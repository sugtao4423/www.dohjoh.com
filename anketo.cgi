#!/usr/local/bin/perl
#
# (C) COPYRIGHT International Business Machines Corp. 1999
# All Rights Reserved
#

#------ sendmailパスの指定 ----------------------------------------------
# 以下の、$mailprogに、サーバー上にある"sendmail"コマンドをフルパスで
# 記入します。詳しくは、プロバイダのガイドに従ってください。
# (例) $mailprog = '/usr/lib/sendmail';
$mailprog = '/usr/lib/sendmail';
#------------------------------------------------------------------------
#------ メールアドレスの指定 ------------------------------------------
# 以下の、$mailtoに、アンケートの送り先となるメールアドレスを記入します。
# (例) $mailto = 'mailaddress@sample.ibm.jp';
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
### 送信フォーマット
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
print "<H2 align=\"center\">アンケートにご協力誠にありがとうございました！</H2>\n";
print "<HR>\n";
print "<P>\n";
print "　あなたの貴重な意見を今後のページ作成に役立てたいと考えています。\n";
print "</BODY></HTML>\n";
