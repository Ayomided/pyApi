from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movies():
    return 'Done', 201


@main.route('/movies')
def movies():
    movies = []
    return jsonify({'movies': movies})