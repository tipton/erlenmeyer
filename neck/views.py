# -*- coding: utf-8 -*-

from flask import render_template, flash, request

from . import neck_app
from .lib_one import show_now

@neck_app.route('/')
def index_func():
    return render_template('landing_page.html')


@neck_app.route('/login_prompt')
def present_login_form():
    return render_template('login_form.html')


@neck_app.route('/check_credentials', methods=['get', 'post'])
def check_login_credentials():
    """
    The login credentials come from the <form> on the login_prompt page.
    <form> data is in the Flask request.form{} dictionary.

    Check the login_prompt.html file to match up the <form> input fields
    with the request.form{} dictionary entries.

    Something to note here: the server receives the user's password as plain
    text - unless some operation is performed on it in the browser.  Even then,
    the server can see, and therefore "knows," the value that comes from the
    user to permit access his account.  The server should take care not to
    "remember" that value; just use it to compute the password hash, and throw
    it away.

    Also, regardless of the detailed reason for login failure, we report only
    the the combination of user_id and password does not work.

    """

    # Look at the stdout stream to see the values coming in from the login form
    print('request.form values from login_form.html')
    for x in request.form:
        print('    {}: {}'.format(x, request.form[x]))


    credentials_ok = True           # Any failed test reverses value to False

    # Check that data entry fields exist and have some value in them

    # if '/check_credentials' route invoked without using login_prompt page
    # then the request.form dictionary will not have expected entries
    if 'user_id' not in request.form:
        credentials_ok = False

    elif 'password' not in request.form:
        credentials_ok = False

    # if one of the request.form login entry fields is left empty
    elif not request.form['user_id']:
        credentials_ok = False

    elif not request.form['password']:
        credentials_ok = False

    # At this point, take the login credentials to do a database check
    #    1. retrieve a user from the database with user_id as the key
    #    2. encrypt the password
    #    3. check that the encrypted password is correct for the user

    elif not user_in_database():
        credentials_ok = False

    elif not user_password_match():
        credentials_ok = False

    if credentials_ok:
        return render_template('action_page.html')

    flash('Username-Password combination not valid.')
    return render_template('login_form.html')


def user_in_database():
    if request.form['user_id'] == 'oops':
        return False
    return True

def user_password_match():
    if request.form['password'] == 'oops':
        return False
    return True

@neck_app.route('/more_action')
def follow_on_action():
    flash('More action selected.')
    return render_template(('action_page.html'))

@neck_app.route('/logout')
def logout_option():
    flash('Logged out.')
    return render_template('login_form.html')
