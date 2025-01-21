# User Requirements for the Journal Software


## General

- The journal will have:
    - A title
    - A masthead page
    - An about page
    - A submissions guidelines page

## People

- Submitting a manuscript creates an account with the role of author.
- Users can edit and delete their own accounts.
- Assigning a referee to a manuscript adds the referee role to that person.
- Only the editor and managing editor(s) have create / update / delete permissions for the accounts of others.
- Advanced: record a history of each user's interacitons with the system.
- A listing of all people is available, but only to the editor and managing editor(s).
- A journal masthead can be generated from the database and displayed by the frontend.

## Text

- All large runs of text in the system, such as "About this Journal" or "Submission Guidelines,"
    are stored in the database.
- Also the journal title can be edited.
- These texts can be edited from the client application, but only by the editor and managing editor(s).

## Manuscripts

- Manuscripts can flow through the system according to [this chart](https://github.com/AthenaKouKou/journal/blob/main/docs/Manuscript_FSM.jpg).
- A dashboard will present the manuscripts in visual form.
- Only the editor and managing editor(s) see all manuscripts; everyone else only sees "their own." That means
    manuscripts for which they are the author or referee.
