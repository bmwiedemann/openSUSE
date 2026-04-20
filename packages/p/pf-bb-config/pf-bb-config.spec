#
# spec file
#
# Copyright (c) 2026 SUSE LLC
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

Name:           pf-bb-config
Version:        25.11
Release:        0
Summary:        Intel pf baseband config tool for ACC100/ACC200/AGX100 accelerator cards
License:        Apache-2.0
Group:          System/Libraries
URL:            https://github.com/intel/pf-bb-config
Source:         pf-bb-config-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
%description
The Physical Function (PF) Baseband Device (BBDEV) Configuration Application 
(pf_bb_config) from Intel to setup the ACC100/ACC200/AGX100 accelerator 
cards.
The program accesses the configuration space and sets various parameters 
through memory-mapped I/O (MMIO) reads and writes.

%prep
%autosetup
sed -i "s/#VERSION_STRING#/%{version}/g" config_app.c

%build
%make_build

%install
install -D -m 0755 pf_bb_config %{buildroot}%{_bindir}/pf_bb_config

out_dir="%{buildroot}/%{_datadir}/pf-bb-config/examples"
install -d $out_dir
find . \( -name "*.cfg" -o -name "*.bin" \) | cpio -pdm --quiet $out_dir

%fdupes %{buildroot}/%{_datadir}/pf-bb-config

%files
%license LICENSE
%defattr(-,root,root,-)
%{_bindir}/pf_bb_config
%dir %{_datadir}/pf-bb-config
%dir %{_datadir}/pf-bb-config/examples
%{_datadir}/pf-bb-config/examples/*

%changelog
