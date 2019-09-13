#
# spec file for package offlineimap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           offlineimap
Version:        7.2.3
Release:        0
Summary:        IMAP/Maildir Synchronization Tool
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://offlineimap.org/
Source0:        https://github.com/OfflineIMAP/offlineimap/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  docutils
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  python2-Sphinx
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
BuildRequires:  systemd-rpm-macros
Requires:       ca-certificates
Requires:       python2
Requires:       python2-curses
Requires:       python2-six
Suggests:       %{name}-htmldoc
Suggests:       python2-gssapi
BuildArch:      noarch

%description
OfflineIMAP is a tool to synchronize IMAP and Maildir mailboxes and
which uses a multithreaded synchronization algorithm. It offers
several user interfaces and is configurable providing a great number
of settings for controlling its behavior. There are several
mechanisms for determining the list of mailboxes to synchronize. It
supports internal or external automation, SSL and PREAUTH tunnels,
offline (or "unplugged") reading, and a variety of esoteric IMAP
features for compatibility with IMAP servers. OfflineIMAP takes
precautions to avoid the loss of mails.

%package htmldoc
Summary:        HTML documentation for %{name}
Group:          Documentation/HTML

%description htmldoc
Separated documentation from %{name} package

%prep
%setup -q
sed -i '/^#!\/usr\/bin\/env/d' offlineimap/bundled_imaplib2.py

%build
python setup.py build
make %{?_smp_mflags} V=1 -C docs

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot} \
    --record-rpm=INSTALLED_FILES

rm -rf docs/html/_sources \
    docs/html/.buildinfo \
    objects.inv

mkdir examples
mv offlineimap.conf* examples

install -D -m 644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -m 644 docs/%{name}ui.7 %{buildroot}%{_mandir}/man7/%{name}ui.7
install -D -m 444 contrib/systemd/%{name}.service %{buildroot}%{_userunitdir}/%{name}.service
install -D -m 444 contrib/systemd/%{name}@.service %{buildroot}%{_userunitdir}/%{name}@.service
install -D -m 444 contrib/systemd/%{name}-oneshot.service %{buildroot}%{_userunitdir}/%{name}-oneshot.service
install -D -m 444 contrib/systemd/%{name}-oneshot.timer %{buildroot}%{_userunitdir}/%{name}-oneshot.timer
install -D -m 444 contrib/systemd/%{name}-oneshot@.service %{buildroot}%{_userunitdir}/%{name}-oneshot@.service
install -D -m 444 contrib/systemd/%{name}-oneshot@.timer %{buildroot}%{_userunitdir}/%{name}-oneshot@.timer
rm docs/html/doctrees/environment.pickle

%files -f INSTALLED_FILES
%license COPYING
%doc Changelog.md README.md examples
%{_mandir}/man?/%{name}*.?%{?ext_man}
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service
%{_userunitdir}/%{name}@.service
%{_userunitdir}/%{name}-oneshot.service
%{_userunitdir}/%{name}-oneshot.timer
%{_userunitdir}/%{name}-oneshot@.service
%{_userunitdir}/%{name}-oneshot@.timer

%files htmldoc
%doc docs/html

%changelog
