#!/usr/bin/perl
#
# Copyright (C) 2017 Thorsten Kukuk
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# in Version 2 or later as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>.
#

=head1 NAME

    create_autoyast_profile - Create autoyast profile for SUSE CaaSP

=head1 SYNOPSIS

    create_autoyast_profile [options]

=head1 DESCRIPTION

    Create an autoyast profile for fully automatic installation of
    SUSE Container as a Service Platform Cluster Node.

=head1 OPTIONS

    -o|--output file    Write autoyast profile as 'file' to disk
    --salt-master       Specify the name of the salt master server
    --ntp-server        Specify name of ntp server
    --smt-url           Specify url of SMT server
    --regcode           Specify registration code for SUSE CaaSP
    --reg-email         Specify email address for registration
    --usage             Print usage
    -h|-?|--help        Help

=cut

use strict;
use warnings;
use locale;
use Pod::Usage;
use Getopt::Long;
use Net::Domain qw(hostname hostfqdn);
use JSON qw(decode_json);

my $outputfile = "-";
my $saltmaster = hostfqdn();
my $ntp_server = "";
my $smturl = "";
my $reg_email = "";
my $regcode = "";
my $help = 0;
my $man = 0;
my $usage = 0;

GetOptions('o|output=s' => \$outputfile,
	   'salt-master=s' => \$saltmaster,
	   'smt-url=s' => \$smturl,
	   'reg-email=s' => \$reg_email,
	   'regcode=s' => \$regcode,
	   'ntp-server=s'=>\$ntp_server,
           'man' => \$man,
           'u|usage' => \$usage,
           'help|h|?' => \$help) or pod2usage(2);
pod2usage(0) if $help;
pod2usage(-exitstatus => 0, -verbose => 2) if $man;
pod2usage(-exitstatus => 0, -verbose => 0) if $usage;



open(OUTPUT,">$outputfile") || die("Can't open output file $outputfile: $!.");

print_header();
print_bootloader();
print_general_section();
print_languages();
setup_networking();
setup_ntp();
print_software();
print_services();
print_scripts();
set_root_password();
setup_registration();
setup_salt_minion();
print_footer();

close(OUTPUT);

#------------------------------------------------------------------------------

sub print_header {
    print OUTPUT <<"HeaderText";
<?xml version="1.0"?>
<!DOCTYPE profile>
<profile xmlns="http://www.suse.com/1.0/yast2ns" xmlns:config="http://www.suse.com/1.0/configns">
HeaderText
}

#------------------------------------------------------------------------------

sub print_footer {
    print OUTPUT <<"EOT";
</profile>
EOT
}

#------------------------------------------------------------------------------

sub print_bootloader {
    print OUTPUT <<"EOT";
  <bootloader>
    <global>
      <generic_mbr>true</generic_mbr>
      <gfxmode>auto</gfxmode>
      <hiddenmenu>false</hiddenmenu>
      <os_prober>false</os_prober>
      <terminal>gfxterm</terminal>
      <timeout config:type="integer">8</timeout>
      <suse_btrfs config:type="boolean">true</suse_btrfs>
    </global>
  </bootloader>
EOT
}

#------------------------------------------------------------------------------

sub print_general_section {
    print OUTPUT <<"EOT";
  <general>
    <ask-list config:type="list"/>
    <mode>
      <confirm config:type="boolean">false</confirm>
      <second_stage config:type="boolean">false</second_stage>
      <self_update config:type="boolean">false</self_update>
    </mode>
    <proposals config:type="list"/>
    <storage>
      <partition_alignment config:type="symbol">align_optimal</partition_alignment>
      <start_multipath config:type="boolean">false</start_multipath>
    </storage>
  </general>
   <partitioning config:type="list">
    <drive>
      <use>all</use>
      <partitions config:type="list">
        <partition>
          <mount>/boot/efi</mount>
          <size>200mb</size>
	  <partition_id config:type="integer">1</partition_id>
          <filesystem config:type="symbol">vfat</filesystem>
        </partition>
        <partition>
          <mount>/</mount>
          <size>30gb</size>
        </partition>
         <partition>
            <filesystem config:type="symbol">btrfs</filesystem>
            <mount>/var/lib/docker</mount>
            <size>max</size>
          </partition>
       </partitions>
    </drive>
  </partitioning>
  <ssh_import>
    <copy_config config:type="boolean">false</copy_config>
    <import config:type="boolean">false</import>
  </ssh_import>
EOT
}

#------------------------------------------------------------------------------

sub print_languages {
    print OUTPUT <<"EOT";
  <keyboard>
    <keymap>english-us</keymap>
  </keyboard>
  <language>
    <language>en_US</language>
    <languages/>
  </language>
  <timezone>
    <hwclock>UTC</hwclock>
    <timezone>Etc/GMT</timezone>
  </timezone>
EOT
}

#------------------------------------------------------------------------------

sub set_root_password {

    my $password = "!";
    my $encrypted = "true";

    open(PASSWD, '/etc/passwd');
    while (<PASSWD>) {
	chomp;
	my($login, $passwd, $uid, $gid, $gcos, $home, $shell) = split(/:/);

	if ($login eq "root") {
	    if ($passwd eq "x") {
		if (open(SHADOW, '/etc/shadow')) {
		while (<SHADOW>) {
		    chomp;
		    my($slogin, $spasswd, $sp_lstchg, $sp_min, $sp_max,
		       $sp_warn, $sp_inact, $sp_expire, $sp_flag) = split(/:/);
		    if ($slogin eq "root") {
			$password = $spasswd;
			$encrypted = "true";
		    }
		}
		close(SHADOW);
                }
	    } else {
		$password = $passwd;
	    }
	}
    }
    close(PASSWD);

    print OUTPUT <<"EOT";
  <users config:type="list">
    <user>
      <username>root</username>
EOT

print OUTPUT "      <user_password>$password</user_password>\n";
print OUTPUT "      <encrypted config:type=\"boolean\">$encrypted</encrypted>\n";

    print OUTPUT <<"EOT"
    </user>
  </users>
EOT
}

#------------------------------------------------------------------------------

sub print_software {
    print OUTPUT <<"EOT";
  <software>
    <image/>
    <install_recommended config:type="boolean">false</install_recommended>
    <instsource/>
    <patterns config:type="list">
      <pattern>SUSE-MicroOS</pattern>
      <pattern>SUSE-MicroOS-hardware</pattern>
      <pattern>SUSE-MicroOS-apparmor</pattern>
      <pattern>SUSE-CaaSP-Stack</pattern>
    </patterns>
  </software>
EOT
}

#------------------------------------------------------------------------------

sub print_services {
    print OUTPUT <<"EOT";
  <services-manager>
    <default_target>multi-user</default_target>
    <services>
      <disable config:type="list">
        <service>purge-kernels</service>
      </disable>
      <enable config:type="list">
        <service>sshd</service>
        <service>cloud-init-local</service>
        <service>cloud-init</service>
        <service>cloud-config</service>
        <service>cloud-final</service>
        <service>issue-generator</service>
        <service>issue-add-ssh-keys</service>
        <service>docker</service>
        <service>container-feeder</service>
EOT
    print OUTPUT "        <service>salt-minion</service>\n" if ($saltmaster ne "");
    print OUTPUT "        <service>systemd-timesyncd</service>\n" if ($ntp_server eq "");
    print OUTPUT <<"EOT";
      </enable>
    </services>
  </services-manager>
EOT
}

#------------------------------------------------------------------------------

sub print_scripts {

    if ($saltmaster ne "" || $ntp_server eq "") {
	print OUTPUT <<"EOT";
  <scripts>
    <chroot-scripts config:type="list">
EOT
    if ($saltmaster ne "") {
	print OUTPUT <<"EOT";
      <script>
        <filename>configure-salt.sh</filename>
        <interpreter>shell</interpreter>
        <chrooted config:type="boolean">true</chrooted>
        <source>
<![CDATA[
#!/bin/sh
EOT
       print OUTPUT "echo \"master: $saltmaster\" > /etc/salt/minion.d/master.conf" if ($saltmaster ne "");
    print OUTPUT <<"EOT";
]]>
        </source>
      </script>
EOT
}
    if ($ntp_server eq "") {
	print OUTPUT <<"EOT";
      <script>
        <filename>configure-timesyncd.sh</filename>
        <interpreter>shell</interpreter>
        <chrooted config:type="boolean">true</chrooted>
        <source>
<![CDATA[
#!/bin/sh
EOT
      my $my_hostname = hostfqdn();
       print OUTPUT "sed -i -e 's|#NTP=.*|NTP=$my_hostname|g' /etc/systemd/timesyncd.conf\n";
    print OUTPUT <<"EOT";
]]>
        </source>
      </script>
EOT
}
	print OUTPUT "    </chroot-scripts>\n";
	print OUTPUT "  </scripts>\n";
    }
}

#------------------------------------------------------------------------------

sub find_smturl {
    if (open(INPUTFILE, "</etc/SUSEConnect")) {
	while (<INPUTFILE>) {
	    chomp;
	    if ( $_ =~ m/^url:/ ) {
		$_ =~ s/url: //;
		close (INPUTFILE);
		return $_;
	    }
	}
    }
    close (INPUTFILE);
    return "";
}

sub setup_registration {
    my $is_active = 0;

    if ($smturl ne "" || $regcode ne "") {
	$is_active = 1;
    } else {
	my $connectoutput = `/usr/sbin/SUSEConnect -s 2>/dev/null`;
	if ($? == 0) {
	    my $decoded = decode_json($connectoutput);
	    foreach my $prod ( @{$decoded} ) {
		if ($prod->{"identifier"} eq "CAASP") {
		    $regcode = $prod->{"regcode"} if ($regcode eq "");
		    $is_active = 1 if ($prod->{"status"} eq "Registered");
		}
	    }
	}
    }

    print OUTPUT "  <suse_register>\n";
    if ($is_active) {
	$smturl = find_smturl() if ($smturl eq "");

	print OUTPUT "    <do_registration config:type=\"boolean\">true</do_registration>\n";
	print OUTPUT "    <email>$reg_email</email>\n" unless ($reg_email eq "");
	print OUTPUT "    <reg_code>$regcode</reg_code>\n" if (defined $regcode && $regcode ne "");
	print OUTPUT "    <install_updates config:type=\"boolean\">true</install_updates>\n";
	print OUTPUT "    <slp_discovery config:type=\"boolean\">false</slp_discovery>\n";
	print OUTPUT "    <reg_server>$smturl</reg_server>\n" if ($smturl ne "");
    } else {
	print OUTPUT "    <do_registration config:type=\"boolean\">false</do_registration>\n";
    }
    print OUTPUT "  </suse_register>\n";
}

#------------------------------------------------------------------------------

sub setup_salt_minion {

    if ($saltmaster ne "") {
	print OUTPUT <<"EOT";
  <files config:type="list">
    <file>
      <file_path>/etc/salt/minion.d/master.conf</file_path>
      <file_contents>
<![CDATA[
EOT
       print OUTPUT "master: $saltmaster\n";
       print OUTPUT <<"EOT";
]]>
      </file_contents>
      <file_owner>root.root</file_owner>
      <file_permissions>640</file_permissions>
    </file>
  </files>
EOT
    }
}

#------------------------------------------------------------------------------

sub setup_networking {
    print OUTPUT <<"EOT";
  <networking>
    <dhcp_options>
      <dhclient_client_id/>
      <dhclient_hostname_option>AUTO</dhclient_hostname_option>
    </dhcp_options>
    <dns>
      <dhcp_hostname config:type="boolean">true</dhcp_hostname>
      <resolv_conf_policy>auto</resolv_conf_policy>
      <write_hostname config:type="boolean">false</write_hostname>
    </dns>
    <interfaces config:type="list">
      <interface>
        <bootproto>dhcp</bootproto>
        <device>eth0</device>
        <dhclient_set_default_route>yes</dhclient_set_default_route>
        <startmode>auto</startmode>
      </interface>
      <interface>
        <bootproto>static</bootproto>
        <device>lo</device>
        <firewall>no</firewall>
        <ipaddr>127.0.0.1</ipaddr>
        <netmask>255.0.0.0</netmask>
        <network>127.0.0.0</network>
        <prefixlen>8</prefixlen>
        <startmode>nfsroot</startmode>
        <usercontrol>no</usercontrol>
      </interface>
    </interfaces>
    <ipv6 config:type="boolean">true</ipv6>
    <keep_install_network config:type="boolean">true</keep_install_network>
    <setup_before_proposal config:type="boolean">true</setup_before_proposal>
    <managed config:type="boolean">false</managed>
    <routing>
      <ipv4_forward config:type="boolean">false</ipv4_forward>
      <ipv6_forward config:type="boolean">false</ipv6_forward>
    </routing>
  </networking>
EOT
}

#------------------------------------------------------------------------------

sub setup_ntp {
    return if ($ntp_server eq "");
    print OUTPUT <<"EOT";
  <ntp-client>
      <configure_dhcp config:type="boolean">false</configure_dhcp>
      <peers config:type="list">
        <peer>
EOT
    print OUTPUT "          <address>$ntp_server</address>\n";
    print OUTPUT <<"EOT";
	  <options>iburst</options>
	  <type>server</type>
	</peer>
    </peers>
    <start_at_boot config:type="boolean">true</start_at_boot>
    <start_in_chroot config:type="boolean">false</start_in_chroot>
  </ntp-client>
EOT
}

#------------------------------------------------------------------------------
