tcl86t.dll      tk86t.dll       _tk_data               &�     �   Htk86t.dll _tk_data\license.terms _tk_data\ttk\utils.tcl _tk_data\ttk\fonts.tcl zlib1.dll _tk_data\ttk\ttk.tcl VCRUNTIME140.dll tcl86t.dll _tk_data\ttk\cursors.tcl _tk_data\text.tcl _tk_data\tk.tcl proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYI_SPLASH_IPC) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR   �   �   R�l   gAMA  ���a    cHRM  z&  ��  �   ��  u0  �`  :�  p��Q<   bKGD � � �����   tIME�8�m�}  %�IDATx��y��՝�?�yj���^�F��E��E@����L4�sF�M��9�����'���F͘�c4��'9I���E6�( Ј�4K�t�����<���Y�еW��s����}�s�w������F���vW 3����<`,P����B�q Z���z�%���N'{��RB�L?���H$���7!�n � ��^�P( �6�۶�"w�|�3
�c0iҤ��R���Y�U(N�l~
��hkk;����<y2�a���������j�収�_L���]__OOO�)��=�\L���j�I`1�(�S)�@�U��f�f[MM���'��	�<y2�˲n~���*Ù��e����z��z�A����d�*��iB�s�P�*��d2����Ah'��L�a`b�s�P䙉Ⱥ=���a�� '��K�S��@��ׂ�`���������\�Q^���d`7�9�ٶ�m��7 O�s�P�۶l�F�4��ΙBQ$.B\�i�eY�����b�� ��,�BB��:G
E��+���!���΍BQd��֬<>�����Pv���<�S(F"c5�I.�b$R���1*F.n-�4���bD���((F4J ���bD���((F4J ���bD���((F4�����I�1�BQt�, [ױ�2�4�a��& �� M �Er�D���?0�AD��4���S�� ��ϫP���{ �c�d̚���ĹgOV=�BQh2���al[e�
��83�������/'4s酏�@�l1D	@q"��� Y�u����x�=��J�@ ����up8�uaY`�da�W$�
!�q��x��iK_�c�J��H'U�l�+ 9v,�	0&L�?������
���v��0��s;!�	ǲdz�5X�pm` ��ǡC8����ގ��Gg'��#�haY2�"
B	`$rܜ�
0�L!��D|�,S�`����y��!��,-A?rǾ}�>�p�s�>���c�(���H"�J�^/��S�\q���IL��UUU�a��aUT`UT`L�Ht�B0M��>�mm�7oƳq#��H���YJ #�Tŷjk�̟O��k�57c�֖פT�1kj0kj�55џH�8xϻ��]�ϦM8:;�0��rD	�l�4��A"������=��*u����ra46b46���p���]��ʕ����O�`���يea�\D-���ۉ57���0�v:1&M4��7�ڶ�ʕ��xCn�ZVVBP8�,��F�n���g?+��g��Ol�<b�����_y��?�Wk+�fFi)�M�6�:�%K��n�3g�f9�i���~�k�����瞣��'���J g��UQA�?�}�݆Y]]�!H�Cr�H&3�+�XVMG��_��籝�R��h����i�`�B	`�cYX� G��=��~ĺn�7�޼9����u�`�X��l�?��[�E2IŊh����`�b��N'�_�*7ߜ�m!��Ʋ����/!�ӛSE������jt������%lG�^�m����������!��ݍK��aȥG��咿{�rG�����d]f]V0����}�����e���pĲH̘A�7��U���D2��ى{���+�;p8��ӃH$ �D��ǚ��U�BZ�l�3�=c�8��S�Ϝ)O���4iwtt�_�r����y-=E�ml����o�8�ܼ%+�Q<�7�_����8D�b��<΢�i�u|����H$�%�����x@��~̆�3fkj"�Ԅ�؈��f�o�58[[�v)7,�ȢE���:/ɉdφ�y�[o�����k^q
�����ڹ��?���������R��^�1y�{-�b�
�3e�W%��Dj�g�_������A�SOQ���G��ҟ��(�=��Յ��ߛob�M����S��͓��S�޴	��M�7b�,b_L��9�ܛ7S��Cx�~[�C1W�N��y�;;�x����Jb�B���O}��ر��]$�T��r�3��+#l��е�ʕ��]K�}��ܵ���T�� �q���e�����g>���7�7gk+�5kr^rU.������{6n�����<+��{����J����2�7ߌ��G�K�ǣ0\�m�]$_Y�>L��?.ߖ�t�Zz׎���2"EP.�\Ě�r��+�[9�n��x4M�U�����ɕ�yC��1kjH̘�u��v*_|1�#g;J �˒~������]+��#�0�q��&$�=��>lYx�}�L��1�%�a� %�,�9�}}8w�zЪ��0!���"�!D�)P�0�V�R��}��~���Ӆm�gr�|[��Mb�#	�XlX�A�(o����������2~em-�׋��`;��XL��B!�#Gл��w����~Q�U�hhZn��t]˲��͔� R�ު�"1m�/$>s&��S1���~��t/�4�b1D$���Wk+���q��>��ּD+fy�D"��{<9�'�V�K ��Nb�4"���23f���2Eױ�~�������oD��ǵc޵k�^�k��{/�^���y�)�@ ����YF*�!�Tŏ�������WK�_*���"U��[���<���h==e)aۈH$����<l�n]���(� R�dC_���9y]2B̺:i���J<�K��g�]++[�l!�_�4��1A|�\x�9�|��ea{<D�,��+_�C�U:��!�`�ٳ�ZE�/~!c̔Ѥ��Յ0��M`�9s0�9G��y�)	�4����O����'��X~?�k�������/˵��*T)��-�a�1a�+�,���ŭu�ky�����c�tSޣ�dCG��_�z�a�_z�~���)%[4���K1&N,���@*�S��@���5���~��:�D�,���G�,^<�%A��^��w�Lb�t���5l�O�ۜ�8H�����.[�Y__��2��Σ������I%�0p�����ҥ�~�krE� =�Ɵ�m�b�t�l=2���Ar�D���圶�K���knF�p���!D�'ǩ����W�vӋ���l���mr�L&���(�jj�͝;���q��55!"<۶_B�E"D,��\  N'�ٳIN��k�N��:��R�R�.�;~�i�K����l����9�]]��o/� D,Fr�hb�\�{z�Fb�Tb�����8��e��&���	�8R�Y�hoǹo����²��nl�WƝ<�\�q�HN��YUU��U����{�E��ƷjUq�om���2p�Mr�<$f̠����
U��?�>� ��#e) ��޺ߪUx6nĹ{7ZO�<�d��}���ÁUY�1a�9s�.X@��);/�iH����}Gw�����h�]�������zkޒ��~�.%z�%T���T,_�s�^9I>˅P�!�P��a|��N�#�P����w���h�ȱJ�i��%Ġi��сg�&�����<Q�Ǽ�55�uu�:Q̉�i���&�hQޅmUVkn&z�eXUU8F�����Te! �L�}�-jz�꧞�����+������c�>|k��ٸ��'9n����ĉh��x6m�{�����Ç�}>�_��	��7��W�;=:�,�,�\ zw7�O<A�~�k�V�%_�̴lG{;�7����Abڴ�ܝ�i睇{�f�����m��wcL�.wv�XUU���!r�$�O��x䈼���|R�P:�6����~*^zIj!�ȩ��҂g�F��Ǔ�0!�d��
�@ ����Z�B#Z8�s�.b_���l�O��X�D~_Uz�<e���t���$���?O��J/'�� ���6�lh��2%��N��s߾�.�
���Gg'��.�����N'ɱc�.X {�)S���+�zðW(� �p���5�=&7`J�O�������Q$�M���9�眃��7���0k���ֆ��)�b�����5��UW�?��-A��;v|s����>�U��űc��"5��lڄ1iƤI9%g��������{E�?D?|������	����lh z�%���J��N��~y�^)l#P4h�05?�U�>+��ˡP�����[I\pAn��	3ߪU�� l���v�&~�X���������1�;�Ȓ%D/��dC�����sl����qE �4�z�i��zJ��S!�~�(���.Z�Sg���lo����E�I 8w���҂1y�<ZZ�r�u̺:b��r�0m²���e$����i��������O@�p�ߏ�r���fB`�\�W�,ފ�I��8p ����.Ɣ)9]A�l����鄯�R�K��=é<�����};�/�(�k�m���#9?>�d��*�＃c߾��q������q� ɉ�%s�nx�N�����r�������@��]
�" g[/���K
BjR���D��"�Hl�ۍv�(���K�,"�Ľ};�u�BȰ(�F��'��9f��Λ�H�Z���"A	�x��y� Ɣ)ri4[�������Y�����x�l�
��4���l�4)�E��͝���ܿ��l%��B���\uU���ߏo�:���7�	��,�{��[�
�Ga��a�UW%�:�s�!z���&��씗�iSM	�dR�B�ٳ����n7ν{�l�P��wMC$�v����8��1����J/R䡩���D/������&�EΛ�ɤN^�N'�+���h�\*�gN��h�֭�_G{;VUf]]Y�VE�y�Ϛ���ǁ�� >�`B!"K�d��$��_F(�^฼�'��-[���/�Z[��^����B��M#9a����q\;wlnP����4��N�[�d��Y_/ݦ�z$�#�G�R�|9�３Qw�A�����U򼛣Gs���Ȳe�c�$���� �q�o��u�[�����<�Yv�nd�B!|�VQ�l��N�'?���"'�����[����_+ϣ�2X+S���mzo/fMMVI$�9G�U.�� �I\۶�ji!��_�7��?M��I5+�w��˱**�������Fo���~𠜄e�1n\YL,�"u8I��⥗u�4�v5=�gÆcV�"kj���I̜���@	����Wkk�I�cƔ��k�倮�%Ԗ��x�1_�*������YԹB|�,��<Ȕ�9���0�;wf�q��J��5�C!l@�������{���6��<���E���XS��_�j�(%��  ����O�+*�)��E �#{L�|�qn���e��^--�&�`�wܑs�*��ȑ�oh��~�a8#�s��.*�{��w�Ũ{����?|�0�t)K���b��p����e7��{<�������R�� �W^a���%����l����o'q�yY��J g@��Y�@[����dғ�H�k�1���w�)�ld����Y�^+���;T$��}>�އ3�m�U��"����	>�8���y���5��K�XU8"����$İ�!/�����?�	����o�70kk	_w]V!/� ΀0�,���8|R�BTz׭c�=���o�j�/Y��ؘ��� 
�mg/��]G���? ���y[)J�s�K.�x�A	��N'v���m��HV�h"���'	>�H֫l' х3�S	�t��v�zcYY�!���0��y������.r|�,�^	 �.Wֱu�eɃ�S#$�T���V��99����ԩYЕ N�mcUVf-ND"�r<VN��U?��4���t?���,�J �A f0��e��� ��ӣ�[Z��$�Nͨ�V86�hc�C ���|�A��AE�u�uu�O� N�2Lb�XO_'�pf4׎�>�(�d�`��R	 �nwN�{��#?�I��9^8hUVf�R�8l+Ę<9�$�w�P0�F$��v���=k;r�Z� 9bY'�=:��k�0��vl5�2v:Pn$�}"��&�yAbs���dhG��ܷO��3!�7����ոCD	�T�6��/��g�����[	 CD4��ʲ ��w%�Sa���$f��:	�֭j(L3��T�adt���Hb2���x,&O@����y��z�7"��d�M	�dl����>�u�ݻ���)*\9����p�N�����Ʋ�ΟOb�����[���Y l��qY[O ����v�� �'~ছ�?d�
0�� �#[�IL��S8I��-S=@V�6�k�!�Ԕu�[qoۦ�?�b�XUU9�=��g&��zKi,K�ظ��'a���OB��-��Ƕ^��X�3s��Ð��3(% ���}_�JN/��{7�7�,X川N�.�ё�&��?t�Yo<�4�>�(��w% �\}N��_~Y�S/���4�57st�2=�(᫯��0�,��\Bxɒ��q���wtd� )X��&z��ͬO~�{V��BaZ�1����1�A�)S������70����X�����N�����ȷj�<`�0DL��8��o�W�`�T._.'`�h�m��u�������Azﺋ�G%v���7!�6V @��w�;7����]�.���a-�h�5?ƤI��>�\�SR���e�_��,�ɓ��ֿq9�хIL�N�W�"��ߢwv�Y�XVe%=��C(ǡ'�w�ڬ��� Fc#�O~R��Ƭ�Ib�4���Z�l��_����i�m����GS�|�����s�]t>�K�ʉ�i�GY�2�&�1]�,�U�zo/�˗g�"-�=�VM��h��k׮c&�b�R��Ft�"��w�9srN���kT?�Da�5Mb�^JϷ�%/�8��9f��.#1s&Z(�����*���@ӈ]tG�?��;��+Wx�٬n�,�(9v,G��m��^J��g���Bꂅ��Z;7�����o���6�d��S��ˉW�[�����_�ݡ~��&r�Ě�����?�w�Z������y#57I����?O��7gm4<�����~%�Rb*j�V��"�x1��f|��N�o�g�D��[��oWTY���/}��ܹ9w� ��~�I��,P�
}��2�eXD/&:>������x׭ùw�����Oz��tbL�@��	�p���"_�e�T��wx�}7랤$����JB����/���T�X�w�z��n�iʍ�l���N��55Ě�	�pх�uy¿b�˗���ķ�ߌ���!6o��f��y�=<o�����}h���L"l�X@�t������FXv*$�9j�Y�do4o���yo(<�6����|'˴K�۪�"�d	хq�څ��w�l؀{�v��.9��,үap�'�`��_�B��c�$bMMD/����|U�����"���L|].�n�5�����lh �������~�{����C\�v�ػ��M�!�q9����t������x0kkI��1q"�ٳ��>ɱcv?���!�?����0�wP��m��Č$f�`���ƹw/Ν;q�ك��!��G��<�c����0�����IL��1aVEEA�w�GQ����ܳ�p;���gW���U]M���_x! �h����ۋ�Ӄ��/�<���H&e�l�������e���jy+f.��?�޷����� ��v:I64�lh8v&�4��qH$d��]?&��(�;ǁ�}�����V�z�����?�	_�ra��`����	E��L�A�/I�s��eߥ�pJt]���8��GGu<�w͚-u�5�d�Y�� ��3T���ǖwsdd[!���������?v�V�p��R��_{ME�;�R��|�Ѽ�[-� l�|w$��k�N�����V��$�ƽm���65?,w�G8zO�=D�'?�{�����T����)Ŷ�������^��Ww'U�����z�)�|��T._>bì�>���e��No"���Pp+������|���Ĵi2tu�#�q*�/�����G�f�4����.|k��ڹ+�=zD�<)b1*_z����aC���/IMC��z�iܛ7�������r��)����|���~'�k��l��!b1�/��w�z����MĚ��QX��۩��/��J��Z��)��@ ��s'�믧��[�ñLZ�����T��縷l4Ε�[����x׬!z�ń������y���Ʊ?��?O��~'O���TܾT����	<��U����3p�$ǎ-�LwK�g����+ǌme"�H���+��{�M�3g����.\���8�n�������T�X���m�5Z�?�LU,�޽y����������<�U�V�4q��Q���K�K/;HR.���H	A���>�i��O�3Gzo���!�k�F����y3��+�Y#[�t�[�w0d�B��hϐ�5m��rʶ4���;�ٹ���#r�U��+(�k��l���?�[�Z�q�V�� �:��
|+Wb�C���57�=��s1��x��4яŵs'�w���v-�?�N�t�S�^WL�4�̵ٶ�}>i,s:���/zo/�?<�gR�q+ 1c�E��͝��؈US����4�p�څw�z����ھ��o������"�<?���S���6Mz�ƏǬ���h�΂��8zO��v\����mýe��v9�L��%jM �}@�L+Y�{4���dC��S1�O�7��ر�&@�g�:[ץI�0��q��~��.������\;vH�o_߱�e9��A�<�mc�tn��H�fC�q�H�s��`TUa�~?��3X���=u�^X�c�L"�Q�HD�yw7���q8���������HWi.6�1t���.r���6��_Rڙ��KO{<��Jc�Λ�����t����)c!�4z<X>�,�Կ�p`k�4#�&�4�K4F�D �HH�AYV��)o���`��;�x����l9�,?��iNuhf����R�䴒"3�yeΆ�p�P% ňF	@1�QP�h� #% ňF	@1�QP�h� #% ňF	@1�QP�h4 �{e�����J���D�4�`�s�P�����ԹP(J�NX��ΉBQdL`���K����t�5۶[��J���ȼg�v��iZxH�:G
E�H/h��,�¶���R�J�(�m�^aY�!D�3 V�)&�L�!�@kkkK��J�;������봵��������`t�s�P�-�7����3\jE�߀�R�T��3������ ��S� �i�i����*u��<��'�L��4�ݻw��	�{{{�����t~`YVp!j8��l�t:�+�7�N Ȟ����0�t]�&3�*F21`9p�aB�k׮������:iҤ��R���<�wT($r��S�jO?�7-�3� nll$������7 s�:Nу(%�#-=�۶�"w�|>���s�9vcc#�a�v�+�Y�|�R�<`,P�+
Õ8� �A��h^l���!��yƊ����쇏l�:   %tEXtdate:create 2023-08-07T18:56:26+00:00[�   %tEXtdate:modify 2023-08-07T18:56:26+00:00*QJ�   WzTXtRaw profile type iptc  x���qV((�O��I�R #.c#K� D�4�d#�T ��������ˀH�J. �t�B5�    IEND�B`�