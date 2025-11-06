from flask import Flask, Blueprint, jsonify, request
from models.aluno_model import AlunoModel

app = Flask(__name__)

