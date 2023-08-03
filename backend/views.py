from flask import Blueprint, session, request, jsonify
import random

api = Blueprint('api', __name__)

@api.route('/game', methods=['GET', 'POST'])
def game_constructor():
    if request.method == 'GET':
        nome_do_jogo = session.get('game')

        if nome_do_jogo:
            return jsonify({'message':'Sala encontrada', 'data':{'game': nome_do_jogo}}), 200
        else:
            return jsonify({'message':'Sala nao encontrada', 'data':{'game': None}}), 404
    else:
        if 'game' not in session:
            session['possibilidades'] = range(1, 11)
            session['game'] = 'sala'

            return jsonify({'message': 'Sala criada', 'data': {'game': 'sala'}}), 201
        return jsonify({'message': 'Sala ja existe', 'data': {'game': 'sala'}}), 400


@api.route('/game/<string:game>', methods=['GET', 'POST'])
def game(game):
    if request.method == 'GET':
        if 'game' not in session:
            return jsonify({'message': 'Sala nao encontrada', 'data': {'game': None}}), 404
        
        if len(session['possibilidades']) == 1:
            del session['game']
            return jsonify({'message': 'Acertei', 'resultado': session['possibilidades'][0]}), 200

        if session.get('quer_perguntar'):
            return jsonify({'message': 'Pergunta'}), 200
        
        chute = random.choice(session['possibilidades'])
        session['numero'] = chute
        return jsonify({'message': 'Chute', 'data': chute}), 200
        

    elif request.method == 'POST':
        corpo = request.get_json()

        if not corpo:
            return jsonify({'message': 'Corpo da requisicao nao encontrado'}), 400

        if not 'resposta_chute' in corpo and not 'resposta_pergunta' in corpo:
            return jsonify({'message': 'Resposta nao encontrada'}), 400
        
        index_do_numero = session['possibilidades'].index(session['numero'])

        if 'resposta_chute' in corpo:
            if corpo['resposta_chute']:
                del session['game']
                return jsonify({'message': 'Acertei'}), 200
            
            if session['numero'] == session['possibilidades'][0]:
                session['possibilidades'] = session['possibilidades'][index_do_numero + 1:]
            elif session['numero'] == session['possibilidades'][-1]:
                session['possibilidades'] = session['possibilidades'][:index_do_numero]
            else:
                session['quer_perguntar'] = True

            return jsonify({'message': 'Errei'}), 200
        
        if 'resposta_pergunta' in corpo:
            if corpo['resposta_pergunta']:
                session['possibilidades'] = session['possibilidades'][index_do_numero + 1:]
            else:
                session['possibilidades'] = session['possibilidades'][:index_do_numero]

            session['quer_perguntar'] = False
            return jsonify({'message': 'Pergunta respondida'}), 200