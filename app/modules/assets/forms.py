#!/usr/bin/python
# -*- coding: utf-8 -*-

# import dependencies
from wtforms import Form, StringField, FileField, TextAreaField, validators, BooleanField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField


from app.modules.users.models import User
from app.modules.items.models import Item
# from app.modules.items.assetitem_model import AssetItem

class Form_Record_Add(Form):

    data_file_name = FileField('data_file_name', validators=(validators.Optional(),))
    data_content_type = StringField('data_content_type', validators=[validators.Length(max=255, message='max 255 characters')])
    data_file_size = StringField('data_file_size', validators=[validators.Length(max=255, message='max 255 characters')])

    asset_type = StringField('asset_type', validators=[validators.Length(max=255, message='max 255 characters')])
    width = IntegerField('width', default=0)
    height = IntegerField('height', default=0)

    description_en_US = TextAreaField('description_en_US',
                                validators=[validators.Length(max=200, message='max 200 characters')])

    description_fr_FR = TextAreaField('description_fr_FR',
                                validators=[validators.Length(max=200, message='max 200 characters')])

    user = QuerySelectField(query_factory=lambda: User.query.filter(User.is_active == True).all(), get_label="username", allow_blank=True)


    items = QuerySelectMultipleField('Select Items',
                             query_factory=lambda : Item.query.filter(Item.is_active == True).all(),
                             get_label=lambda s: s.title_en_US,
                             allow_blank=True)

    is_active = BooleanField('is_active', default=True)


