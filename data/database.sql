DROP DATABASE IF EXISTS WebStore;
CREATE DATABASE WebStore;
USE WebStore;


-- -----------------------------------------------------------------------------
-- - Construction de la table des utilisateurs                               ---
-- -----------------------------------------------------------------------------
CREATE TABLE T_Users (
    idUser              int         PRIMARY KEY AUTO_INCREMENT,
    login               varchar(20) NOT NULL,
    password            varchar(20) NOT NULL,
    connectionNumber    int         NOT NULL DEFAULT 0
);

INSERT INTO T_Users (idUser, login, password) VALUES ( 1, 'Anderson',   'Neo' );
INSERT INTO T_Users (idUser, login, password) VALUES ( 2, 'Skywalker',  'Luke' );
INSERT INTO T_Users (idUser, login, password) VALUES ( 3, 'Plissken',   'Snake' );
INSERT INTO T_Users (idUser, login, password) VALUES ( 4, 'Ripley',     'Ellen' );
INSERT INTO T_Users (idUser, login, password) VALUES ( 5, 'Bond',       'James' );

SELECT * FROM T_Users;

-- -----------------------------------------------------------------------------
-- - Construction de la table des informations des utilisateurs                                                       ---
-- -----------------------------------------------------------------------------
CREATE TABLE T_UserInformations (
    idInformations  int      PRIMARY KEY AUTO_INCREMENT,
    idUser          int      NOT NULL REFERENCES T_Users(idUser),
    address         text,
    city            text,
    email           text,
    phoneNumber     text
);

INSERT INTO T_UserInformations (idUser, address, city, email, phoneNumber) 
VALUES ( 1, 'Inconnue', 'La matrice', 'neo@matrix.com', '1234567890' ),
       ( 2, 'rue du Faucon', 'L''étoile noire', 'luke@glaforce.wars', '0147258369' ),
       ( 3, '1997, Manhattan', 'New York', 'snake@carpenter.com', '9638527410' ),
       ( 4, 'Nostromo', 'La bas', 'ripley@nostromo.alien', '9876543210' ),
       ( 5, 'SIS Building', 'London', '007@mi6.uk', '7007007007' );

SELECT * FROM T_UserInformations;

-- -----------------------------------------------------------------------------
-- - Construction de la table des rôles                                      ---
-- -----------------------------------------------------------------------------

CREATE TABLE T_Roles (
    idRole       int         PRIMARY KEY AUTO_INCREMENT,
    roleName     varchar(20) NOT NULL
);

INSERT INTO T_Roles (roleName)
VALUES ('client'), ('admin'), ('stockManager');

SELECT * FROM T_Roles;

-- -----------------------------------------------------------------------------
-- - Construction de la table d'association T_Users/T_Roles                  ---
-- -----------------------------------------------------------------------------

CREATE TABLE T_Users_Roles_Associations (
    idUser   int    NOT NULL REFERENCES T_Users(idUser),
    idRole   int    NOT NULL REFERENCES T_Roles(idRole)
);

INSERT INTO T_Users_Roles_Associations 
VALUES (1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (5, 2);

SELECT * FROM T_Users_Roles_Associations;

-- -----------------------------------------------------------------------------
-- - Construction de la tables des articles en vente                         ---
-- -----------------------------------------------------------------------------
CREATE TABLE T_Articles (
    idArticle           int         PRIMARY KEY AUTO_INCREMENT,
    description         varchar(30) NOT NULL,
    brand               varchar(30) NOT NULL,
    unitaryPrice        double      NOT NULL
);

INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Souris',                  'Logitoch',             65 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Clavier',                 'Microhard',            49.5 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Systeme d''exploitation', 'Fenetres Vistouille',  150 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Tapis souris',            'ATP Formation',        5 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Cle USB 8 To',            'Syno',                 8 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Laptop',                  'PH',                   1199 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'CD x 500',                'CETME',                250 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'DVD-R x 100',             'CETME',                99 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'DVD+R x 100',             'CETME',                105 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Batterie Laptop',         'PH',                   80 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'Casque Audio',            'Syno',                 105 );
INSERT INTO T_Articles ( description, brand, unitaryPrice ) VALUES ( 'WebCam',                  'Logitoch',             755 );

SELECT * FROM T_Articles;

-- -----------------------------------------------------------------------------
-- - Construction des tables des commandes et des lignes de commandes        ---
-- -----------------------------------------------------------------------------
CREATE TABLE T_Commands (
    idCommand       int         PRIMARY KEY AUTO_INCREMENT,
    idUser          int         NOT NULL REFERENCES T_Users(idUser),
    commandDate     datetime    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE T_CommandLines (
    idCommandLine   int     PRIMARY KEY AUTO_INCREMENT,
    idCommand       int     NOT NULL REFERENCES T_Commands(idCommand),
    idArticle       int     NOT NULL REFERENCES T_Articles(idArticle),
    quantity        int     NOT NULL
);

-- Une première commande
INSERT INTO T_Commands (idUser, commandDate) VALUES ( 2, now() ); 
INSERT INTO T_CommandLines (idCommand, idArticle, quantity) VALUES (1, 1, 5); 
INSERT INTO T_CommandLines (idCommand, idArticle, quantity) VALUES (1, 3, 3);

-- Une seconde commande, pour un admin
INSERT INTO T_Commands (idUser, commandDate) VALUES ( 1, now() ); 
INSERT INTO T_CommandLines (idCommand, idArticle, quantity) VALUES (2, 2, 4); 
INSERT INTO T_CommandLines (idCommand, idArticle, quantity) VALUES (2, 3, 1);
INSERT INTO T_CommandLines (idCommand, idArticle, quantity) VALUES (2, 4, 1);

-- -----------------------------------------------------------------------------
-- - Construction de la table des paiements                                  ---
-- -----------------------------------------------------------------------------

CREATE TABLE T_Payments (
    idPayment           int          PRIMARY KEY AUTO_INCREMENT,
    idCommand           int          NOT NULL REFERENCES T_Commands(idCommand),
    amount              double       NOT NULL,
    paymentDate         datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO T_Payments (idCommand, amount, paymentDate) 
VALUES ( 1, 775, now() ),
       ( 2, 353, now() );

SELECT * FROM T_Payments;

-- -----------------------------------------------------------------------------
-- - Construction de la table des paiements paypal                           ---
-- -----------------------------------------------------------------------------

CREATE TABLE T_PaypalPayments (
    idPayment           int          NOT NULL REFERENCES T_Payments(idPayment),
    accountNumber       varchar(30)
);

INSERT INTO T_PaypalPayments VALUES ( 1, 'A fake paypal account' );

SELECT * FROM T_PaypalPayments;

-- -----------------------------------------------------------------------------
-- - Construction de la table des paiements par cartes bleues                ---
-- -----------------------------------------------------------------------------

CREATE TABLE T_CreditCardPayments (
    idPayment           int          NOT NULL REFERENCES T_Payments(idPayment),
    cardNumber          char(24),
    expirationDate      varchar(5)
);

INSERT INTO T_CreditCardPayments VALUES ( 2, '1234 5678 9012 3456', '06/19' );

SELECT * FROM T_CreditCardPayments;
