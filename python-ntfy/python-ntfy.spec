#
# spec file for package python-ntfy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Matthias Bach <marix@marix.org>.
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-ntfy
Version:        2.7.0
Release:        0
Summary:        A utility for sending push notifications
License:        GPL-3.0-only
Group:          Development/Languages/Python
Url:            https://github.com/dschep/ntfy
Source:         ntfy-%{version}.tar.xz
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# test requirements
BuildRequires:  %{python_module emoji}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module sleekxmpp}
BuildRequires:  fdupes
Requires:       python-appdirs
Requires:       python-requests
Requires:       python-ruamel.yaml
Suggests:       python-sleekxmpp
Suggests:       python-dnspython3
Suggests:       python-slacker
Suggests:       python-telegram-send
Suggests:       python-psutil
Suggests:       python-instapush
Suggests:       python-rocketchat-API
Suggests:       python-emoji
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
ntfy brings notification to your shell. It can automatically provide
desktop notifications when long running commands finish or it can send
push notifications to your phone when a specific command finishes.

Quickstart
----------

    $ ntfy send test
    # send a notification when the command `sleep 10` finishes
    # this sends the message '"sleep 10" succeeded in 0:10 minutes'
    $ ntfy done sleep 10

%prep
%setup -q -n ntfy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/ntfy*

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/ntfy
%{python_sitelib}/*

%changelog
