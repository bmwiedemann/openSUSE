#
# spec file for package python-ntfy
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-ntfy
Version:        2.7.1
Release:        0
Summary:        A utility for sending push notifications
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/dschep/ntfy
Source:         ntfy-%{version}.tar.xz
# https://github.com/dschep/ntfy/issues/247
Patch0:         python-ntfy-no-mock.patch
Patch2:         drop-misleading-shebangs.patch
BuildRequires:  %{python_module appdirs}
# test requirements
BuildRequires:  %{python_module emoji >= 1.6.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-appdirs
Requires:       python-requests
Requires:       python-ruamel.yaml
Suggests:       python-dnspython3
Suggests:       python-emoji >= 1.6.2
Suggests:       python-instapush
Suggests:       python-psutil
Suggests:       python-rocketchat-API
Suggests:       python-slack-sdk
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ntfy
%python_expand %fdupes %{buildroot}%{$python_sitelib}/ntfy*

%check
export XDG_CONFIG_HOME=/foo/config
# There is an isolation error. Somewhere in the tests the default configuration dict is modified.
# For the normal application execution that is not an issue as configuration is loaded only once.
# So this is the hacky workaround until the issue is fixed upstream.
%pytest --ignore 'tests/test_xmpp.py' -k 'not test_xmpp' --ignore 'tests/test_config.py'
%pytest --ignore 'tests/test_xmpp.py' -k 'not test_xmpp' 'tests/test_config.py'

%pre
%python_libalternatives_reset_alternative ntfy

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/ntfy
%{python_sitelib}/ntfy
%{python_sitelib}/ntfy-%{version}*-info

%changelog
