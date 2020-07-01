#
# spec file for package python-pygn
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pygn
Version:        0.10.2
Release:        0
License:        GPL-3.0
Summary:        The Python Gateway Script: news2mail mail2news gateway
Url:            https://gitlab.com/mcepl/pyg
Group:          Productivity/Networking/News/Utilities
Source:         https://files.pythonhosted.org/packages/source/p/pygn/pygn-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module rply}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
Python Gateway Script from news to mail and vice versa.

It is intended to be a full SMTP/NNTP rfc compliant gateway
with whitelist manager.

You will probably have to install a mail-transport-agent and/or
news-transport-system package to manage SMTP/NNTP traffic.

MTA is needed for mail2news service, since mail have to be
processed on a box where pyg is installed. You can use a remote
smtpserver for news2mail.

News system is useful but not needed, since you can send articles to a
remote SMTP server (ie: moderated NG) where is installed pyg, otherwise you
will need it.

It refers to rfc 822 (mail) and 850 (news).

%prep
%setup -q -n pygn-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pygm2n
%python_clone -a %{buildroot}%{_bindir}/pygn2m
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pygm2n pygn2m

%postun
%python_uninstall_alternative pygm2n pygn2m

%files %{python_files}
%{python_sitelib}/*
%python_alternative %{_bindir}/pygm2n
%python_alternative %{_bindir}/pygn2m

%changelog
