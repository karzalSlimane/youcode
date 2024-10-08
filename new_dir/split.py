
emails = [
    "utilisateur1@example.com",
    "utilisateur2@example.com",
    "utilisateur3@test.com",
    "utilisateur4@example.com",
    "utilisateur5@test.com",
    "utilisateur6@sample.com"
]

domaines = [email.split('@')[1] for email in emails]

domaines_uniques = set(domaines)

print(domaines_uniques)
