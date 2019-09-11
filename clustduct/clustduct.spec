#
# spec file for package clustduct
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


#
%define tftpdir /srv/tftpboot

%bcond_with pdfdoc

Name:           clustduct
Version:        0.0.4
Release:        0
Summary:        Framework which connects a genders database to dnsmasq
License:        BSD-3-Clause
Group:          System/Management
Source0:        https://github.com/mslacken/clustduct/archive/v%{version}.tar.gz#/clustduct-%{version}.tar.gz
Source1:        clustduct-rpmlintrc
Url:            https://github.com/mslacken/clustduct   
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  dnsmasq
BuildRequires:  lua
BuildRequires:  lua-genders
%if %{with pdfdoc}
%if 0%{?is_opensuse}
BuildRequires:  pandoc
BuildRequires:  texlive-latex
%endif
%endif
Requires:       bc
Requires:       dnsmasq
Requires:       genders
Requires:       lua-genders
Requires:       lua53-luaposix
%ifarch x86_64
Requires:       grub2-x86_64-efi
Requires:       shim
Requires:       syslinux
BuildRequires:  grub2-x86_64-efi
BuildRequires:  shim
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      apparmor
Recommends:     python3-kiwi
Recommends:     git

%description
This framework feeds dnsmasq with the node information of a genders
database. It can also create a PXE boot file structure with the possiblity to
update node MAC addresses in the genders database. In addition, boot images
can be managed in the PXE environment.

%prep
# macro for removing nested directories
%define sanitize_dir() _uglydir=$(ls -d *); shopt -s dotglob;mv $_uglydir/* .; rmdir $_uglydir
%setup -q -c -n %{name}-%{version}
%sanitize_dir  %{name}-%{version}

%build
%if %{with pdfdoc} && 0%{?is_opensuse}
for file in *.md ; do 
	pandoc -o ${file%%md}pdf $file
done
%endif

autoreconf -i
%configure

%install
%make_install

%files
%defattr(-,root,root)
%if %{with pdfdoc} && 0%{?is_opensuse}
%doc *.pdf
%endif
%license COPYING

%{_sbindir}/clustduct.lua
%{_sbindir}/write_bf.lua
%{_sbindir}/prepare_tftp.sh
%config %{_sysconfdir}/clustduct.d/
%config %{_sysconfdir}/clustduct.conf
%{_datadir}/doc/%{name}
%if !%{is_opensuse}
%exclude %{_datadir}/doc/%{name}/kiwi-descriptions/openSUSE/
%endif 
%exclude %{_datadir}/doc/%{name}/COPYING
%{_libdir}/lua

%changelog
