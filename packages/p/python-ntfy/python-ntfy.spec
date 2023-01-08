#
# spec file for package python-ntfy
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Matthias Bach <marix@marix.org>.
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
Name:           python-ntfy
Version:        2.7.0
Release:        0
Summary:        A utility for sending push notifications
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/dschep/ntfy
Source:         ntfy-%{version}.tar.xz
# https://github.com/dschep/ntfy/issues/247
Patch0:         python-ntfy-no-mock.patch
Patch1:         emoji-2.0-compatibility.patch
Patch2:         drop-misleading-shebangs.patch
Patch3:         python-311-compat.patch
BuildRequires:  %{python_module appdirs}
# test requirements
BuildRequires:  %{python_module emoji >= 1.6.2}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
Requires:       python-requests
Requires:       python-ruamel.yaml
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-dnspython3
Suggests:       python-emoji >= 1.6.2
Suggests:       python-instapush
Suggests:       python-psutil
Suggests:       python-rocketchat-API
Suggests:       python-slacker
Suggests:       python-sleekxmpp
Suggests:       python-telegram-send
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
%autosetup -p1 -n ntfy-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ntfy
%python_expand %fdupes %{buildroot}%{$python_sitelib}/ntfy*

%check
%pytest --ignore 'tests/test_xmpp.py' -k 'not test_xmpp'

%post
%python_install_alternative ntfy

%postun
%python_uninstall_alternative ntfy

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/ntfy
%{python_sitelib}/*

%changelog
