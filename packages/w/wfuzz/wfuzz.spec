#
# spec file for package wfuzz
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           wfuzz
Version:        3.1.0
Release:        0
Summary:        The web fuzzer
License:        GPL-2.0-only
URL:            https://wfuzz.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/w/wfuzz/wfuzz-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives

%python_subpackages

%description

Wfuzz has been created to facilitate the task in web applications assessments
and it is based on a simple concept: it replaces any reference to the FUZZ
keyword by the value of a given payload.

A payload in Wfuzz is a source of data.

This simple concept allows any input to be injected in any field of an HTTP
request, allowing to perform complex web security attacks in different web
application components such as: parameters, authentication, forms,
directories/files, headers, etc.

Wfuzz is more than a web content scanner:

* Wfuzz could help you to secure your web applications by finding and
  exploiting web application vulnerabilities. Wfuzz’s web application
  vulnerability scanner is supported by plugins.

* Wfuzz is a completely modular framework and makes it easy for even the newest
  of Python developers to contribute. Building plugins is simple and takes
  little more than a few minutes.

* Wfuzz exposes a simple language interface to the previous HTTP
  requests/responses performed using Wfuzz or other tools, such as Burp. This
  allows you to perform manual and semi-automatic tests with full context and
  understanding of your actions, without relying on a web application scanner
  underlying implementation.


It was created to facilitate the task in web applications assessments, it's a
tool by pentesters for pentesters ;)

%prep
%autosetup -p1 -n wfuzz-%{version}
sed -i '1{/^#!/ d}' src/wfuzz/wfuzz.py
sed -i 's/pyparsing>=2.4\*/pyparsing>=2.4/g' setup.py

%build
%python_build

%install
%python_install

for p in wfencode wfpayload wfuzz wxfuzz ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative wfencode wfpayload wfuzz wxfuzz

%postun
%python_uninstall_alternative wfencode wfpayload wfuzz wxfuzz

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%python_alternative %{_bindir}/wfencode
%python_alternative %{_bindir}/wfpayload
%python_alternative %{_bindir}/wfuzz
%python_alternative %{_bindir}/wxfuzz

%changelog
