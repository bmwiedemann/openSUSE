#
# spec file for package coccigrep
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           coccigrep
Version:        1.17+git.20180322
Release:        0
Summary:        Semantic grep tool for C, based on coccinelle
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://home.regit.org/software/coccigrep/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.xz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  xz
Requires:       coccinelle
Requires:       python3
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description
coccigrep is a semantic grep for the C language based on coccinelle. It can be
used to find where a given structure is used in code files. coccigrep depends on
the spatch program which comes with coccinelle.

%prep
%setup -q
chmod 644 README.rst

%build
python3 setup.py build
gzip -c coccigrep.1 > coccigrep.1.gz

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

install -d $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m 644 coccigrep.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.rst ChangeLog
%{python3_sitelib}/*
%{_bindir}/coccigrep
%{_mandir}/man1/coccigrep.1*

%changelog
