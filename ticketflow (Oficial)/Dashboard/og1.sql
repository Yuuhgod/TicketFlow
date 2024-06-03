PGDMP      	                |         
   OG1 System    16.2    16.2     �           0    0    ENCODING    ENCODING     #   SET client_encoding = 'SQL_ASCII';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    49168 
   OG1 System    DATABASE     �   CREATE DATABASE "OG1 System" WITH TEMPLATE = template0 ENCODING = 'SQL_ASCII' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "OG1 System";
                postgres    false                        2615    57669    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            �           0    0    SCHEMA public    COMMENT         COMMENT ON SCHEMA public IS '';
                   postgres    false    5            �           0    0    SCHEMA public    ACL     +   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
                   postgres    false    5            �            1259    57686    cadparceiro    TABLE     �   CREATE TABLE public.cadparceiro (
    codigoparceiro integer NOT NULL,
    a_descricao character varying(100),
    endereco character varying(200),
    telefone character varying(20)
);
    DROP TABLE public.cadparceiro;
       public         heap    postgres    false    5            �            1259    57691    cadsolicitacao    TABLE       CREATE TABLE public.cadsolicitacao (
    ordemsolicitacao integer NOT NULL,
    data date,
    descricao character varying(200),
    situacao character varying(30),
    situacaosuporte character varying(30),
    codigoparceiro integer,
    correcaosuporte character varying(200)
);
 "   DROP TABLE public.cadsolicitacao;
       public         heap    postgres    false    5            �          0    57686    cadparceiro 
   TABLE DATA           V   COPY public.cadparceiro (codigoparceiro, a_descricao, endereco, telefone) FROM stdin;
    public          postgres    false    215   5       �          0    57691    cadsolicitacao 
   TABLE DATA           �   COPY public.cadsolicitacao (ordemsolicitacao, data, descricao, situacao, situacaosuporte, codigoparceiro, correcaosuporte) FROM stdin;
    public          postgres    false    216   �                  2606    57690    cadparceiro cadparceiro_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.cadparceiro
    ADD CONSTRAINT cadparceiro_pkey PRIMARY KEY (codigoparceiro);
 F   ALTER TABLE ONLY public.cadparceiro DROP CONSTRAINT cadparceiro_pkey;
       public            postgres    false    215                        2606    57695 "   cadsolicitacao cadsolicitacao_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.cadsolicitacao
    ADD CONSTRAINT cadsolicitacao_pkey PRIMARY KEY (ordemsolicitacao);
 L   ALTER TABLE ONLY public.cadsolicitacao DROP CONSTRAINT cadsolicitacao_pkey;
       public            postgres    false    216            !           2606    57696 1   cadsolicitacao cadsolicitacao_codigoparceiro_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cadsolicitacao
    ADD CONSTRAINT cadsolicitacao_codigoparceiro_fkey FOREIGN KEY (codigoparceiro) REFERENCES public.cadparceiro(codigoparceiro);
 [   ALTER TABLE ONLY public.cadsolicitacao DROP CONSTRAINT cadsolicitacao_codigoparceiro_fkey;
       public          postgres    false    4638    215    216            �   M  x���Kn�0D��)x�����%#3��JEً��?G���E����3��Q�q`I9`Tx�p���C^������lu?5Fk�2=��E��]�0������q/�&k�5f��:��7Z�Q����v����>Ā{����^��8	�*ۙ����K�����K�=1�	ư���i�v}�]'��x����]�,�=#�O�Q m*6(N^�s�'q����x��g��SH�w���C?TrTWd�[�\�g��b8��t�]v�fku%fuX`Ó�?�Im�}H@80�=�6 �Y�\�4Z��K�"WQÅV��̌R]�K�r^�;����5_m�4߫��F      �   �  x��UMo�0=ۿB����&=�[؀a-vڅ�G�,z������Ĳ�&v�m����^e�b��)�7�*�H�uڃp��(��;�������V`*��T�Aï˂G�,z��]8��2`$*Ky���x�;��/H��(�r�x��c#8!�(�o;��$�Z�-:���<%��D#!��ֿ���3�T��@Gz���h�}=\�hhI�p��An�m ٪��:�*�/��u�f��V�X��[^��*���b���jC�O�ڱB��e��a�,h�� /�	o�R�
�]D�1��rͳ�n��PP�%õ�`�j��+�u�`�'�~(��"م��Gi8溄��<�/ޤ�و}ܻ$��t����S?+>~�����ኦZ��?��rC>)��d�Կ�B9���kϥ���)����w���W���g	m��I��jԽK�f���F +��|����q]K��ҷ���g���cY0�2������&�y>�l�E�[EL�:�w�8�a��zw@�6A�vX��nC�X;�7�]��b=5�j��{�o��~K�Gi���!���C��RX���ʡ�C$[V�N�Le>��ĐJ�m�. ^n��Iέ�4A|| ��k�z������6z=V���j������A=��0�ix��e�@��t-ʐ�x�q� W�_U��Ɔ��A4��!�?#S�S�~��R��}������E     