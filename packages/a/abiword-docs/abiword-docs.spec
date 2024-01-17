#
# spec file for package abiword-docs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           abiword-docs
Version:        3.0.2
Release:        0
Summary:        A Multiplatform Word Processor - Documentation
License:        GPL-2.0
Group:          Productivity/Office/Word Processor
Url:            http://www.abisource.com/
Source0:        http://abisource.com/downloads/abiword/latest/source/%{name}-%{version}.tar.gz
BuildRequires:  abiword >= 3.0.2
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  libabiword-3_0-devel
Requires:       abiword
Supplements:    abiword
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
AbiWord is a multiplatform word processor with a GTK+ interface on the
UNIX platform. For extended functionality and integration, this version
is compiled with GNOME support. Abiword with the GNOME front-end is
part of the GNOME Office Suite.

%prep
# 3.0.2 tarball from upstream is broken, extracts to previous version, please fix on next release.
%setup -q -n abiword-docs-3.0.1

%build
export XDG_RUNTIME_DIR=/tmp
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes %{buildroot}

%files
%defattr(-, root, root)
%doc %{_datadir}/abiword-3.0/help/

%changelog
