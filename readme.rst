#########################
Duplicate_dilemma
#########################

********
Personas
********

Grace is an 87 year old head of a non-profit business. For decades, the 
office has run the same way. Computers were used, but not to their full 
capabilities. A younger volunteer has suggested updating the company’s 
website and developing an email marketing list. She has multiple paper 
mailing lists for snail mail as far back as 1996. Grace would love to 
eliminate the pages and pages of duplicates efficiently, reduce her 
postal costs and move into the twenty-first century.


*****************
Problem Scenarios
*****************

Grace searches through the list eliminating each duplicate manually which
wastes  time and money.


Current Alternatives
====================

Creating a program to digitize the list and eliminate the duplicates. Also, 
creating a system to match fields and weed out extraneous information, 
as well as counting and generating separate list to categorize clients.


Value Proposition
==================

By creating a program to digitized contact files and search for duplicated 
contacts, Grace could more efficiently and effectively market her clients. 


************
User Stories
************

As Grace the business owner, I want to easily consolidate and access my 
vast list of contacts, so that I can utilize email and/or web mailing programs 
and reduce my mailing cost.


*****************
Acceptance Story
*****************

| **Scenario 1:** Inputting the contact
| **Given** that I have a digitized/scanned OCR list
| **And** I have exported that list into a database
| **When** I import the file
| **Then** the contact duplicates will be eliminated
| **And** a new main list will be generated
| 

| **Scenario 2:** Categorizing the contacts
| **Given** that I have different types of mailing lists
| **And** I would like to use specific parameters
| **When** I open the category function
| **Then** I will be able to input the email address,
| enter the parameters ( *General*, *Special Mailing*  or *Subscriber*)
|**And** the list will generate the updated parameter
| 

| **Scenario 3:** Deleting the contacts
| **Given** that people unsubscribe to mailing list
| **And** I would like to delete the contact
| **When** I open the delete function
| **Then** I will be able to input the email address 
| **And** when prompted, enter *Yes* to delete the contact 
| 
