-- 기본 설정
-- CREATE DATABASE amazon;
-- USE amazon;

-- 1) customers 테이블에 새 고객을 추가하세요.
-- CREATE TABLE customers
-- (
-- 	name VARCHAR(10) NOT NULL,
--     age INT NULL,
--     address VARCHAR(50) NOT NULL,
--     phone VARCHAR(20) NOT NULL
-- );
INSERT INTO customers(name, age, address, phone)
VALUES ('홍길동', 24, '대전 유성구', '01012334537');

-- 2) products 테이블에 새 제품을 추가하세요.
CREATE TABLE products
(
	name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    stock INT,
    brand VARCHAR(50),
    category VARCHAR(50)
);
INSERT INTO products(name, price, stock, brand, category)
VALUES ('고양이 헤드셋', 99000, 300, '네코미', '전자기기');