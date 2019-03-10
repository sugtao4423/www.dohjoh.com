#!/usr/local/bin/perl
#
# (C) COPYRIGHT International Business Machines Corp. 1999
# All Rights Reserved
#

#------ sendmail�p�X�̎w�� ----------------------------------------------
# �ȉ��́A$mailprog�ɁA�T�[�o�[��ɂ���"sendmail"�R�}���h���t���p�X��
# �L�����܂��B�ڂ����́A�v���o�C�_�̃K�C�h�ɏ]���Ă��������B
# (��) $mailprog = '/usr/lib/sendmail';
$mailprog = '/usr/lib/sendmail';
#------------------------------------------------------------------------
#------ ���[���A�h���X�̎w�� ------------------------------------------
# �ȉ��́A$mailto�ɁA�A���P�[�g�̑����ƂȂ郁�[���A�h���X���L�����܂��B
# (��) $mailto = 'mailaddress@sample.ibm.jp';
$mailto = '';
#------------------------------------------------------------------------


require 'jcode.pl';

#Get the input
read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

#Split the name-value pairs
@pairs = split (/&/,$buffer);

foreach $pair(@pairs)
{
    ($name, $value) = split(/=/, $pair);

    #Un-Webify plus signs and %-encoding
    $value=~tr/+/ /;
    $value=~s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;

    $FORM{$name} = $value;
    if ( $name ne "to" ) {
       push (@fields, $name) unless (grep(/^$name$/, @fields));
    }
}

#
### ���M�t�H�[�}�b�g
#

$mail_msg = "";

foreach $field (@fields) {
    $mail_msg = "$mail_msg-----------------------------------------------\n";
    $mail_msg = "$mail_msg($field) $FORM{$field}\n";
}
$mail_msg = "$mail_msg-----------------------------------------------\n";

#
### ShiftJis to Jis
#
&jcode'convert(*mail_msg, 'jis');
open(MAIL,"| $mailprog $mailto")|| die "Can't open $mailprog!\n";
print MAIL $mail_msg;
close(MAIL);
#
### Make the person feel good for writing to us
#
print "Content-type: text/html\n\n";
print "<HTML><HEAD><TITLE>Thank you!</TITLE></HEAD>\n";
print "<BODY bgcolor=\"#9dffff\">\n";
print "<H2 align=\"center\">�A���P�[�g�ɂ����͐��ɂ��肪�Ƃ��������܂����I</H2>\n";
print "<HR>\n";
print "<P>\n";
print "�@���Ȃ��̋M�d�Ȉӌ�������̃y�[�W�쐬�ɖ𗧂Ă����ƍl���Ă��܂��B\n";
print "</BODY></HTML>\n";
