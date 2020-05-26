create database if not exists cine_db;

use cine_db; 

create table if not exists usuarios (
	id_usuario int not null auto_increment,
    u_pnombre varchar(35) not null,
    u_apellido varchar(35) not null,
    u_email varchar(20) not null,
    u_password varchar(8) not null,
    u_admin boolean not null,
    primary key(id_usuario)
)engine = innodb;

create table if not exists peliculas(
	id_pelicula int not null auto_increment,
    p_titulo varchar(40) not null,
    p_genero varchar(40) not null,
    p_descripcion varchar(250),
    primary key(id_pelicula)
)engine = innodb;

create table if not exists salas(
	id_sala int not null auto_increment,
    s_num_filas int not null,
    s_num_asientosf int not  null,
    s_tipo varchar(35),
    primary key (id_sala)
)engine = innodb;

create table if not exists funciones(
	id_funcion int not null auto_increment,
    f_fecha_hora  datetime not null,
    f_precio float not null,
    id_pelicula int not null,
    id_sala int not null,
    primary key(id_funcion),
    constraint fkpelicula_funciones foreign key (id_pelicula)
		references peliculas(id_pelicula)
        on delete cascade
        on update cascade, 
	constraint fksala_funciones foreign key (id_sala)
		references salas(id_sala)
		on delete cascade
        on update cascade
)engine = innodb;

create table if not exists asientos(
	id_asiento varchar(2) not null,
    id_funcion int not null,
    a_estado bool not null,
    primary key(id_asiento, id_funcion),
	constraint fkfuncion_asientos foreign key (id_funcion)
		references funciones(id_funcion)
        on delete cascade
        on update cascade
)engine = innodb;

create table if not exists compras (
	id_compra int not null auto_increment,
    c_total_compra float not null,
    id_usuario int not null,
    primary key(id_compra),
    constraint fkusuario_compras foreign key(id_usuario)
    references usuarios(id_usuario)
    on delete cascade
    on update cascade
)engine = innodb;

create table if not exists boletos (
	id_asiento varchar(2) not null,
    id_funcion int not null,
    id_compra int not null,
    primary key (id_asiento, id_funcion, id_compra),
    constraint fkasiento_boletos foreign key(id_asiento)
    references asientos(id_asiento)
    on delete cascade
    on update cascade,
    constraint fkfuncion_boletos foreign key(id_funcion)
    references asientos(id_funcion)
    on delete cascade
    on update cascade,
    constraint fkcompra_boletos foreign key(id_compra)
    references compras(id_compra)
    on delete cascade
    on update cascade
)engine = innodb;

INSERT INTO usuarios (`u_pnombre`, `u_apellido`, `u_email`, `u_password`, `u_admin`) VALUES ('admin', 'admin', 'admin@gmail.com', '1234567a', 1);

INSERT INTO salas (`s_num_filas`,`s_num_asientosf`, `s_tipo`) VALUES (4, 4, 'chica');
INSERT INTO salas (`s_num_filas`,`s_num_asientosf`, `s_tipo`) VALUES (5, 5, 'mediana');
INSERT INTO salas (`s_num_filas`,`s_num_asientosf`, `s_tipo`) VALUES (6, 6, 'grande');

INSERT INTO peliculas (`p_titulo`, `p_genero`, `p_descripcion`) VALUES ('interestellar', 'ciencia ficcion', 'El amor atraviesa dimensiones');
INSERT INTO peliculas (`p_titulo`, `p_genero`, `p_descripcion`) VALUES ('kill bill vol.1', 'accion', 'Black Mamba se vengara');
INSERT INTO peliculas (`p_titulo`, `p_genero`, `p_descripcion`) VALUES ('django', 'accion', 'Rompiendo cadenas y cabezas');

INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 11:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 12:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 13:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 14:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 01:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 11:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 12:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 13:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 23:00:00', 40, 1, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 10:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 11:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 12:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 13:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-24 14:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 01:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 11:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 12:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 13:00:00', 40, 2, 1);
INSERT INTO funciones (`f_fecha_hora`,`f_precio`,`id_pelicula`,`id_sala`) VALUES ('2020-05-25 23:00:00', 40, 2, 1);


