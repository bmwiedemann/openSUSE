# OTRS config file (automaticaly generated!)
# VERSION:1.1
package Kernel::Config::Files::ZZZAuto;
use utf8;
sub Load {
    my ($File, $Self) = @_;
$Self->{'SecureMode'} =  1;
$Self->{'DefaultCharset'} =  'utf-8';
$Self->{'DefaultLanguage'} =  'de';
$Self->{'LogModule'} =  'Kernel::System::Log::File';
$Self->{'Package::RepositoryList'} =  {
  'file://@OTRS_ROOT@/itsm/packages5/' => '[--OTRS::ITSM 5 local repo]',
  'http://ftp.otrs.org/pub/otrs/itsm/packages5/' => '[--OTRS::ITSM 5 Master--] http://ftp.otrs.org/',
  'file://@OTRS_ROOT@/itsm/packages6/' => '[--OTRS::ITSM 6 local repo]',
  'http://ftp.otrs.org/pub/otrs/itsm/packages6/' => '[--OTRS::ITSM 6 Master--] http://ftp.otrs.org/'
};
$Self->{'Package::RepositoryAccessRegExp'} =  '127\\.0\\.0\\.1';
}
1;
