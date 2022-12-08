#
# spec file for package python-pygn
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-pygn
Version:        0.10.2
Release:        0
Summary:        The Python Gateway Script: news2mail mail2news gateway
License:        GPL-3.0-only
Group:          Productivity/Networking/News/Utilities
URL:            https://gitlab.com/mcepl/pyg
Source:         https://files.pythonhosted.org/packages/source/p/pygn/pygn-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rply}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
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
%autosetup -p1 -n pygn-%{version}

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
%{python_sitelib}/mail2news.py
%{python_sitelib}/news2mail.py
%{python_sitelib}/whitelist.py
%{python_sitelib}/wlp.py
%{python_sitelib}/wlp_parser.py
%{python_sitelib}/pygn-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%python_alternative %{_bindir}/pygm2n
%python_alternative %{_bindir}/pygn2m

%changelog
