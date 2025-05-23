
CREATE TABLE public.categories (
	id int4 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL,
	category_name varchar NOT NULL,
	CONSTRAINT categories_pk PRIMARY KEY (id),
	CONSTRAINT categories_unique UNIQUE (category_name)
);


CREATE TABLE public.goods (
	id int4 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL,
	good_name varchar NOT NULL,
	CONSTRAINT goods_pk PRIMARY KEY (id),
	CONSTRAINT goods_unique UNIQUE (good_name)
);

CREATE TABLE public.checks_info (
	shop varchar NOT NULL,
	doc_id varchar NOT NULL,
	item int4 NOT NULL,
	category int4 NOT NULL,
	amount int4 NOT NULL,
	price numeric NOT NULL,
	discount numeric NOT NULL,
	CONSTRAINT checks_info_pk PRIMARY KEY (shop, doc_id, item, category, amount, price, discount)
);

-- public.checks_info внешние включи

ALTER TABLE public.checks_info ADD CONSTRAINT checks_info_categories_fk FOREIGN KEY (category) REFERENCES public.categories(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE public.checks_info ADD CONSTRAINT checks_info_goods_fk FOREIGN KEY (item) REFERENCES public.goods(id) ON DELETE CASCADE ON UPDATE CASCADE;