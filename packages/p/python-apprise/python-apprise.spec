#
# spec file for package python-apprise
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Paolo Panto <munix9@googlemail.com>
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with    libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-apprise
Version:        1.9.2
Release:        0
Group:          Development/Libraries/Python
Summary:        A simple wrapper to many popular notification services used today
License:        BSD-2-Clause
URL:            https://github.com/caronc/apprise
Source0:        https://files.pythonhosted.org/packages/source/a/apprise/apprise-%{version}.tar.gz
Source99:       %{name}.rpmlintrc
%if 0%{?suse_version} <= 1500
BuildRequires:  %{python_module dataclasses}
Requires:       python-dataclasses
%endif
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module click >= 5.0}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module paho-mqtt}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-Markdown
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-click >= 5.0
Requires:       python-requests
Requires:       python-requests-oauthlib
Recommends:     python-paho-mqtt
Suggests:       python-dbus-python
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
Apprise is a Python package for simplifying access to all of the different
notification services that are out there. Apprise opens the door and makes
it easy to access:

Apprise API, APRS, AWS SES, AWS SNS, Bark, Boxcar, Burst SMS, BulkSMS, BulkVS,
ClickSend, DAPNET, DingTalk, Discord, E-Mail, Emby, Faast, FCM, Flock,
Google Chat, Gotify, Growl, Guilded, Home Assistant, httpSMS, IFTTT, Join,
Kavenegar, KODI, Kumulos, LaMetric, Line, MacOSX, Mailgun, Mastodon,
Mattermost,Matrix, MessageBird, Microsoft Windows, Microsoft Teams, Misskey,
MQTT, MSG91, MyAndroid, Nexmo, Nextcloud, NextcloudTalk, Notica, Notifiarr,
Notifico, ntfy, Office365, OneSignal, Opsgenie, PagerDuty, PagerTree,
ParsePlatform, PopcornNotify, Prowl, Pushalot, PushBullet, Pushjet, PushMe,
Pushover, PushSafer, Pushy, PushDeer, Reddit, Rocket.Chat, RSyslog, SendGrid,
ServerChan, Signal, SimplePush, Sinch, Slack, SMSEagle, SMS Manager, SMTP2Go,
SparkPost, Super Toasty, Streamlabs, Stride, Synology Chat, Syslog,
Techulus Push, Telegram, Threema Gateway, Twilio, Twitter, Twist, XBMC,
Voipms, Vonage, WeCom Bot, WhatsApp, Webex Teams.

%prep
%autosetup -n apprise-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 packaging/man/apprise.1

%python_clone -a %{buildroot}%{_bindir}/apprise
%python_clone -a %{buildroot}%{_mandir}/man1/apprise.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_plugin_matrix_attachments_api_v2 and not test_apprise_attachment_truncate and not test_plugin_dbus'

%pre
%python_libalternatives_reset_alternative apprise

%post
%python_install_alternative apprise apprise.1%{?ext_man}

%postun
%python_uninstall_alternative apprise

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/apprise
%python_alternative %{_mandir}/man1/apprise.1%{?ext_man}
%{python_sitelib}/apprise
%{python_sitelib}/apprise-%{version}.dist-info

%changelog
