#
# spec file for package nmap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _buildshell /bin/bash
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define with_system_lua 0%{?suse_version} >= 1330
# don't build python2 subpackages (zenmap, ndiff) because of the python2 deprecation in Tumbleweed
%if 0%{?suse_version} > 1500
%define with_python2 0
%else
%define with_python2 1
%endif
Name:           nmap
Version:        7.70
Release:        0
Summary:        Network exploration tool and security scanner
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
Url:            https://nmap.org/
Source:         https://nmap.org/dist/nmap-%{version}.tar.bz2
Source1:        https://svn.nmap.org/nmap/docs/nmap_gpgkeys.txt#/%{name}.keyring
Source2:        http://nmap.org/dist/sigs/%{name}-%{version}.tar.bz2.asc
Patch1:         nmap-7.40-desktop_files.patch
Patch2:         nmap-4.75-nostrip.patch
Patch3:         su-to-zenmap.patch
Patch4:         nmap-ncat-skip-network-tests.patch
Patch5:         nmap-7.70-CVE-2018-15173_pcre_limits.patch
Patch6:         nmap-7.70-fix_infinite_loop.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
%if %{with_system_lua}
%if 0%{?suse_version} > 1320
BuildRequires:  Lua(devel) = 5.3
%else
BuildRequires:  pkgconfig(lua) >= 5.3
%endif
%endif

%description
Nmap ("Network Mapper") is a utility for network exploration or
security auditing. It may as well be used for tasks such as network
inventory, managing service upgrade schedules, and monitoring host or
service uptime. Nmap uses raw IP packets to determine what hosts are
available on the network, what services (application name and
version) those hosts are offering, what operating systems (and OS
versions) they are running, what type of packet filters/firewalls are
in use, and dozens of other characteristics. It scans large networks,
nad works fine against single hosts.

%package -n zenmap
Summary:        A graphical front-end for Nmap
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Requires:       python-gtk
Obsoletes:      %{name}-gtk < %{version}
Provides:       %{name}-gtk = %{version}-%{release}

%description -n zenmap
zenmap is a graphical front-end for the nmap network scanner

%package -n ndiff
Summary:        Compare results of Nmap scans
Group:          Productivity/Networking/Diagnostic

%description -n ndiff
Ndiff is a tool to aid in the comparison of Nmap scans. It takes two Nmap XML
output files and prints the differences between them: hosts coming up and down,
ports becoming open or closed, etc.

%package -n ncat
Summary:        Network tool to concatenate and redirect sockets
Group:          Productivity/Networking/Diagnostic

%description -n ncat
Ncat is a networking utility which will read and write data across a
network from the command line. It uses both TCP and UDP for
communication and provides network connectivity to other applications
and users.

%package -n nping
Summary:        Packet generator
Group:          Productivity/Networking/Diagnostic

%description -n nping
Nping is a tool for network packet generation, response
analysis and response time measurement. Nping allows to generate network
packets of a wide range of protocols, letting users to tune virtually
any field of the protocol headers. While Nping can be used as a simple
ping utility to detect active hosts, it can also be used as a raw packet
generator for network stack stress tests, ARP poisoning, Denial of
Service attacks, route tracing, etc.

%prep
%setup -q
%if %{with_python2}
%patch1 -p1
%endif
%patch2
%if %{with_python2}
%patch3
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p1

# use system provided libraries
rm -rf libpcap libpcre macosx mswin32

%if %{with_python2}
#fix locale dir
mv zenmap/share/zenmap/locale zenmap/share
sed -i -e "s|^locale_dir =.*$|locale_dir = os.path.join('share','locale')|" \
 -e 's|join(self.install_data, data_dir)|join(self.install_data, "share")|' zenmap/setup.py
sed -i 's|^LOCALE_DIR = .*|LOCALE_DIR = join(prefix, "share", "locale")|' zenmap/zenmapCore/Paths.py
%endif

#fix pt_PT/pt zh/zh_CN locale
sed -i '/ALL_LINGUAS =/s/pt_PT/pt/' Makefile.in
sed -i '/ALL_LINGUAS =/s/zh/zh_CN/' Makefile.in
mv docs/man-xlate/nmap-pt_PT.1 docs/man-xlate/nmap-pt.1
mv docs/man-xlate/nmap-zh.1 docs/man-xlate/nmap-zh_CN.1

%build
export CFLAGS="%{optflags} -DOPENSSL_LOAD_CONF"
export CXXFLAGS="%{optflags} -DOPENSSL_LOAD_CONF"

%configure --with-libpcap=%{_prefix}  \
           --with-libdnet=included    \
%if %{with_system_lua}
           --with-liblua=%{_prefix}   \
%else
           --with-liblua=included     \
%endif
           --with-libpcre=%{_prefix}  \
%if %{with_python2} < 1
           --without-zenmap           \
           --without-ndiff            \
%endif
           STRIP=/bin/true

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} deskdir="%{_datadir}/gnome/apps/Utilities/" install
install -d "%{buildroot}%{_datadir}/pixmaps/"

%if %{with_python2}
rm "%{buildroot}%{_bindir}/uninstall_zenmap"
rm "%{buildroot}%{_bindir}/uninstall_ndiff"
ln -s ../zenmap/pixmaps/zenmap.png "%{buildroot}%{_datadir}/pixmaps/zenmap.png"
%suse_update_desktop_file zenmap System Network
%suse_update_desktop_file zenmap-root System Network
%find_lang zenmap
touch -r %{buildroot}/%{python_sitelib}/zenmapCore/Paths.py %{buildroot}/%{python_sitelib}/zenmapCore/Paths.pyc
%endif
dos2unix %{buildroot}%{_datadir}/%{name}/nselib/data/oracle-sids

%fdupes -s %{buildroot}

%check

pushd ncat
make %{?_smp_mflags} check
popd

pushd libdnet-stripped
make %{?_smp_mflags} check
popd

# retrieve list of compiled in modules
compiled_with=$("%{buildroot}%{_bindir}/nmap" -V | grep "Compiled with:" )
# for the following tests, the leading space is relevant
# check features built with system libraries
[[ $compiled_with == *\ libpcre-* ]]
[[ $compiled_with == *\ libpcap-* ]]
[[ $compiled_with == *\ openssl-* ]]
# check features built with included sources
[[ $compiled_with == *\ nmap-libdnet-* ]]
# check for lua
%if %{with_system_lua}
[[ $compiled_with == *\ liblua-5.3* ]]
%else
# lua in nmap tarball identifies itself as "liblua-5.3.3"
[[ $compiled_with == *\ liblua-5.3.3* ]]
%endif
#

%files
%license COPYING*
%doc CHANGELOG HACKING
%doc docs/README
%doc docs/nmap.usage.txt
%dir %{_mandir}/??
%dir %{_mandir}/??/man1
%dir %{_mandir}/??_??
%dir %{_mandir}/??_??/man1
%{_mandir}/man1/nmap.1%{?ext_man}
%{_mandir}/*/man1/*
%{_bindir}/nmap
%{_datadir}/nmap

%if %{with_python2}
%files -n zenmap -f zenmap.lang
%{_bindir}/xnmap
%{_bindir}/zenmap
%{_bindir}/nmapfe
%{python_sitelib}/zenmap-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/zenmapCore
%{python_sitelib}/zenmapGUI
%{python_sitelib}/radialnet
%{_datadir}/applications/zenmap-root.desktop
%{_datadir}/applications/zenmap.desktop
%{_datadir}/pixmaps/zenmap.png
%{_datadir}/zenmap
%{_mandir}/man1/zenmap.1%{?ext_man}

%files -n ndiff
%{_bindir}/ndiff
%{_mandir}/man1/ndiff.1%{?ext_man}
%{python_sitelib}/ndiff.*
%endif

%files -n ncat
%{_bindir}/ncat
%{_mandir}/man1/ncat.1%{?ext_man}
%dir %{_datadir}/ncat
%config(noreplace) %{_datadir}/ncat/ca-bundle.crt

%files -n nping
%{_bindir}/nping
%{_mandir}/man1/nping.1%{?ext_man}

%changelog
