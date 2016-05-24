#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Duplicate dilemma.

   A program to eliminate duplicates from comma separated contact information
   files with fields: lname, fname, email and category. It formats uploaded
   file then checks duplicates against the original contact file and appends to
   that list. It then exports data to a comma separated file for
   uploading into other programs.
"""

import csv
import os


def get_contacts(filename):
    """A csv import dictionary function.

    Args:
        filename (csv): A comma delimited file.

    Returns:
        Dict: Keyed by email with first and last name, company,
              and category.

    Examples:
        >>>
        {'sjohns@aol.com': {'lname': 'Johns', 'category': 'General',
        'company': '', 'fname': 'Stacey'}}, 'jdoe@gmail.com': {'lname': 'Doe',
        'category': 'General', 'company': '', 'fname': 'Jane'}}
    """
    feeder_dict = {}
    new_dict = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['email'] is not '':
                if row['lname'] is '' and row['fname'] is '':
                    row['lname'] = 'Recipient'
                if row['category'] is '':
                    row['category'] = 'General'
                row['email'] = row['email'].lower()
                row['fname'] = row['fname'].title()
                row['lname'] = row['lname'].title()
                row['company'] = row['company'].title()
                row['category'] = row['category'].title()
                feeder_dict = {row['email']: {'lname': row['lname'],
                                              'fname': row['fname'],
                                              'company': row['company'],
                                              'category': row['category']}}
            new_dict.update(feeder_dict)
    csvfile.close()
    return new_dict


def checkit(newdict):
    """Checks for dups against main contact dictionary and appends.

    Args:
        filename (dict): Default=new_dict.

    Returns:
        Dict: Combined updated no dups dictionary.

    Examples:
        >>>checkit(NEW_DICT)
        {'sjohns@aol.com': {'lname': 'Johns', 'category': 'General',
                            'company': '', 'fname': 'Stacey'},
         'jdoe@gmail.com': {'lname': 'Doe', 'category': 'Subscriber',
                            'company': '', 'fname': 'Jane'}}
    """
    contacts = {}
    try:
        new_path = os.path.join('updatedcontacts.csv')
        with open(new_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts = {row['email']: {'lname': row['lname'],
                                           'fname': row['fname'],
                                           'company': row['company'],
                                           'category': row['category']}}
                if row['email'] not in newdict:
                    newdict.update(contacts)
        csvfile.close()
    except IOError:
        print 'No main contact file exists. Creating new file.'
    return newdict


def writeit(h_dict):
    """Writes CONTACT dictionary to main csv file ((updatedcontacts.csv).

    Args:
        h_dict: dictionary of contacts
    """
    headers = ['email', 'lname', 'fname', 'company',
               'category']
    new_path = os.path.join('updatedcontacts.csv')
    with open(new_path, 'w') as ncf:
        csv_write = csv.DictWriter(ncf, fieldnames=headers,
                                   delimiter=',')
        csv_write.writeheader()
        rows = []
        for key, row in h_dict.iteritems():
            dline = {header:
                     row[header] if header in row else '' for header in headers}
            dline['email'] = key
            rows.append(dline)
        for newrow in rows:
            csv_write.writerow(newrow)
    ncf.close()
    print 'The main contact file has been updated.'


def start():
    """Initiates input of new CSV file. Elimates duplicates and
       writes to main csv file (updatedcontacts.csv).

    Args:
       None
    """
    filename = raw_input('Name of the csv. file to check against main? ')
    writeit(checkit(get_contacts(filename)))


def delete():
    """Deletes contact for main contact list (updatedcontacts.csv).

    Args:
        None
    """
    print 'WARNING: THIS FUNCTION CANNOT BE UNDONE.'
    f_mail = raw_input('Enter email address of contact to delete. ')
    contacts = open_main()
    try:
        contacts.pop(f_mail)
        writeit(contacts)
    except KeyError:
        print 'Email does not exist.'


def categories():
    """Writes new category description to 'updatedcontacts.csv' file

    Args:
       None
    """
    f_mail = raw_input('Enter email address to change category. ')
    contacts = open_main()
    try:
        if contacts[f_mail] is not False:
            print 'The current category is', contacts[f_mail]['category']
        f_cat = raw_input('Enter category.'
                          '(General, Special Mailing or Subscriber) ').title()
        if (f_cat ==
                'General') or (f_cat == 'Special Mailing') or (f_cat ==
                                                               'Subscriber'):
            contacts[f_mail]['category'] = f_cat.title()
            writeit(contacts)
        else:
            print 'Incorrect user category. Restart function.'
    except KeyError:
        print 'Email does not exist. Restart function.'


def open_main():
    """Opens and reads 'updatedcontacts.csv' into CONTACT dict keyed
       by email adress.

    Args:
        None.

    Returns:
        dict: CONTACTS.

    Examples:
        >>>xxx
        {'sjohns@aol.com': {'lname': 'Johns', 'category': 'General',
                            'company': '', 'fname': 'Stacey'},
         'jdoe@gmail.com': {'lname': 'Doe', 'category': 'Subscriber',
                            'company': '', 'fname': 'Jane'}}
    """
    contacts = {}
    ncontacts = {}
    try:
        new_path = os.path.join('updatedcontacts.csv')
        with open(new_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts = {row['email']: {'lname': row['lname'],
                                           'fname': row['fname'],
                                           'company': row['company'],
                                           'category': row['category']}}
                ncontacts.update(contacts)
        csvfile.close()
    except IOError:
        print 'No main contact file exists.'
    return ncontacts

if __name__ == '__main__':
    print 'To upload csv file type start().'
    print 'To delete contact type delete().'
    print 'To change category type categories().'
