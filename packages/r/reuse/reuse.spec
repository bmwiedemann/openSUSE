#
# spec file for package reuse
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Free Software Foundation Europe e.V.
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


%bcond_without test
Name:           reuse
Version:        0.3.3
Release:        0
Summary:        A tool for compliance with the REUSE Initiative recommendations
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://git.fsfe.org/reuse/reuse
Source:         https://files.pythonhosted.org/packages/source/f/fsfe-reuse/fsfe-reuse-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  python3-setuptools
%if %{with test}
BuildRequires:  python3-Jinja2
BuildRequires:  python3-chardet
BuildRequires:  python3-click
BuildRequires:  python3-debian
BuildRequires:  python3-pytest
BuildRequires:  python3-recommonmark
%endif
Requires:       python3 >= 3.5
Requires:       python3-chardet
Requires:       python3-debian
Recommends:     git
Recommends:     python3-pygit2
Recommends:     %{name}-lang
BuildArch:      noarch

%lang_package

%description
A tool for compliance with the REUSE Initiative recommendations.  Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
%setup -q -n fsfe-reuse-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{$python3_sitelib}
%find_lang %{name} %{?no_lang_C}
%if %{with test}
%check
LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=%{buildroot}%{python3_sitelib} py.test tests/
%endif

%files
%defattr(-,root,root,-)
%doc  README.md LICENSES/*
%{_bindir}/reuse
%{python3_sitelib}/*

%files lang -f %{name}.lang

%changelog
