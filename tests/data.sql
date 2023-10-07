INSERT INTO user (username, password, email)
VALUES
    ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f', 'test@test.com'),
    ('test2', '434535stfgswfg5354t', 'test2@test.com');

INSERT INTO menu (category, special)
VALUES
    ('menu1', 0),
    ('menu2', 1); 

INSERT INTO item (author_id, category, code, dish, price, notes, spicy)
VALUES
    (1, 'menu1', 'v43','ret34','yhd','ythdh',0),
    (0, 'menu2', 'c23','h6t','ydh','ygdhh',0),
    (1, 'menu3', 'd45','6wuj','gf','hjdfn',1);
