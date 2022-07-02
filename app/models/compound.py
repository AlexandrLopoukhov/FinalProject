from flask import Flask, jsonify, request
from config import db
import yaml
import os


class Compound(db.Model):
    """Class represents table model"""
    __tablename__ = 'compound'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    compound = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    formula = db.Column(db.String(200), nullable=False)
    inchi = db.Column(db.String(200), nullable=False)
    inchi_key = db.Column(db.String(200), nullable=False)
    smiles = db.Column(db.String(200), nullable=False)
    cross_links_count = db.Column(db.Integer(), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name)for c in self.__table__.columns}

    def as_formated_dict(self, field_width):
        compound_dict = self.as_dict()
        return {k: str(v)[:field_width:]+'...' if len(str(v)) > field_width+3 else v for (k, v) in compound_dict.items()}

