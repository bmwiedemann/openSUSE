#
# spec file for package python-stomp.py
#
# Copyright (c) 2020 SUSE LLC
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


%define skip_python2 1
Name:           python-stomp.py
Version:        6.0.0
Release:        0
Summary:        Python STOMP client
License:        Apache-2.0
URL:            https://github.com/jasonrbriggs/stomp.py
Source0:        https://files.pythonhosted.org/packages/source/s/stomp.py/stomp.py-%{version}.tar.gz
# using github archive for docs
Source1:        https://github.com/jasonrbriggs/stomp.py/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docopt >= 0.6.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python client library for accessing messaging servers (such as ActiveMQ, Apollo or RabbitMQ) using the STOMP protocol versions 1.0, 1.1 and 1.2. It can also be run as a standalone, command-line client for testing.

%prep
%setup -q -n stomp.py-%{version}
%setup -q -n stomp.py-%{version} -D -b 1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/stomp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative stomp

%postun
%python_uninstall_alternative stomp

%files %{python_files}
%doc README CHANGELOG
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/stomp

%changelog
