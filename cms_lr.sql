/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/10/30 21:38:25                          */
/*==============================================================*/


drop table if exists AdmissionsForms;

drop table if exists bookborrow;

drop table if exists bookinfo;

drop table if exists chooseCur;

drop table if exists clazz;

drop table if exists course;

drop table if exists grade;

drop table if exists login;

drop table if exists major;

drop table if exists stuinfo;

drop table if exists teacherInfo;

drop table if exists techcourse;

/*==============================================================*/
/* Table: AdmissionsForms                                       */
/*==============================================================*/
create table AdmissionsForms
(
   sid                  int not null,
   cname                int,
   sname                varchar(12) not null,
   indate               date not null,
   inscore              decimal(8,2) not null,
   agent                varchar(12) not null,
   primary key (sid)
);

/*==============================================================*/
/* Table: bookborrow                                            */
/*==============================================================*/
create table bookborrow
(
   id                   int not null auto_increment,
   bid                  int not null,
   sid                  int not null,
   borrowdate           date not null,
   returndate           date not null,
   operator             int not null,
   primary key (id)
);

/*==============================================================*/
/* Table: bookinfo                                              */
/*==============================================================*/
create table bookinfo
(
   bid                  int not null,
   bname                varchar(12) not null,
   author               varchar(12) not null,
   category             varchar(12) not null,
   publication          varchar(12) not null,
   pubdate              date not null,
   bnum                 int not null,
   indate               date not null,
   price                decimal(8,2) not null,
   intro                varchar(100) not null,
   operator             varchar(12) not null,
   primary key (bid)
);

/*==============================================================*/
/* Table: chooseCur                                             */
/*==============================================================*/
create table chooseCur
(
   sid                  int not null,
   curid                int not null,
   score                decimal(8,2),
   id                   int not null auto_increment,
   primary key (id)
);

/*==============================================================*/
/* Table: clazz                                                 */
/*==============================================================*/
create table clazz
(
   cid                  int not null auto_increment,
   cname                varchar(24) not null,
   gid                  int,
   mid                  int,
   primary key (cid)
);

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course
(
   curid                int not null,
   curname              varchar(12) not null,
   examdate             date not null,
   examtype             varchar(12) not null,
   primary key (curid)
);

/*==============================================================*/
/* Table: grade                                                 */
/*==============================================================*/
create table grade
(
   gid                  int not null,
   gname                varchar(10) not null,
   primary key (gid)
);

/*==============================================================*/
/* Table: login                                                 */
/*==============================================================*/
create table login
(
   uaccount             varchar(12) not null,
   upwd                 varchar(12) not null,
   uname                varchar(12) not null,
   primary key (uaccount)
);

/*==============================================================*/
/* Table: major                                                 */
/*==============================================================*/
create table major
(
   mid                  int not null auto_increment,
   mname                varchar(12) not null,
   primary key (mid)
);

/*==============================================================*/
/* Table: stuinfo                                               */
/*==============================================================*/
create table stuinfo
(
   sid                  int not null,
   identityNum          varchar(18) not null,
   gender               varchar(5) not null,
   birthdate            date not null,
   address              varchar(20) not null,
   age                  int not null,
   tel                  varchar(11) not null,
   politicstatus        varchar(12) not null,
   health               varchar(12) not null,
   primary key (sid)
);

/*==============================================================*/
/* Table: teacherInfo                                           */
/*==============================================================*/
create table teacherInfo
(
   tid                  int not null auto_increment,
   mid                  int,
   tname                varchar(12) not null,
   gender               varchar(5) not null,
   age                  int not null,
   married              varchar(12) not null,
   idnum                varchar(18) not null,
   politicstatus        varchar(10) not null,
   nation               varchar(12) not null,
   edu                  varchar(12) not null,
   birthdate            date not null,
   tel                  varchar(11) not null,
   workdate             date not null,
   description          varchar(200) not null,
   primary key (tid)
);

/*==============================================================*/
/* Table: techcourse                                            */
/*==============================================================*/
create table techcourse
(
   tid                  int not null,
   curid                int not null,
   id                   int not null auto_increment,
   primary key (id)
);

alter table AdmissionsForms add constraint FK_Reference_14 foreign key (cname)
      references clazz (cid) on delete restrict on update restrict;

alter table bookborrow add constraint FK_Reference_11 foreign key (bid)
      references bookinfo (bid) on delete restrict on update restrict;

alter table bookborrow add constraint FK_Reference_17 foreign key (sid)
      references stuinfo (sid) on delete restrict on update restrict;

alter table chooseCur add constraint FK_Reference_12 foreign key (sid)
      references stuinfo (sid) on delete restrict on update restrict;

alter table chooseCur add constraint FK_Reference_7 foreign key (curid)
      references course (curid) on delete restrict on update restrict;

alter table clazz add constraint FK_Reference_15 foreign key (mid)
      references major (mid) on delete restrict on update restrict;

alter table clazz add constraint FK_Reference_16 foreign key (gid)
      references grade (gid) on delete restrict on update restrict;

alter table stuinfo add constraint FK_Reference_4 foreign key (sid)
      references AdmissionsForms (sid) on delete restrict on update restrict;

alter table teacherInfo add constraint FK_Reference_13 foreign key (mid)
      references major (mid) on delete restrict on update restrict;

alter table techcourse add constraint FK_Reference_8 foreign key (tid)
      references teacherInfo (tid) on delete restrict on update restrict;

alter table techcourse add constraint FK_Reference_9 foreign key (curid)
      references course (curid) on delete restrict on update restrict;

