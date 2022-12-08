#
# spec file for package weblate
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


%define WLDIR %{_datadir}/weblate
%define WLDATADIR %{_localstatedir}/lib/weblate
%define WLETCDIR %{_sysconfdir}/weblate
%define _name Weblate
%define skip_python310 1
Name:           weblate
Version:        4.14.2
Release:        0
Summary:        Web-based translation tool
License:        GPL-3.0-or-later
URL:            https://weblate.org/
Source0:        https://dl.cihar.com/weblate/%{_name}-%{version}.tar.xz
Source1:        https://dl.cihar.com/weblate/%{_name}-%{version}.tar.xz.asc
# GPG key from Michal Čihař
# Fingerprint 63CB 1DF1 EF12 CF2A C0EE 5A32 9C27 B313 42B7 511D
# https://cihar.com/.well-known/openpgpkey/hu/wmxth3chu9jfxdxywj1skpmhsj311mzm
Source2:        %{name}.keyring
BuildRequires:  bitstream-vera
BuildRequires:  borgbackup >= 1.1.11
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  git-review >= 1.27.0
BuildRequires:  git-svn
BuildRequires:  gpg2
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  mercurial >= 5.2
BuildRequires:  postgresql
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython >= 0.29.14
BuildRequires:  python3-Django >= 3.2
BuildRequires:  python3-GitPython >= 2.1.15
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-Pillow >= 9.0.0
BuildRequires:  python3-Pygments >= 2.6.0
BuildRequires:  python3-Sphinx >= 1.8
BuildRequires:  python3-aeidon >= 1.9
BuildRequires:  python3-bleach >= 3.1.1
BuildRequires:  python3-boto3 >= 1.15.0
BuildRequires:  python3-celery >= 5.0.3
BuildRequires:  python3-chardet
BuildRequires:  python3-charset-normalizer >= 2.0.12
BuildRequires:  python3-cssselect >= 1.2
BuildRequires:  python3-dbm
BuildRequires:  python3-diff_match_patch = 20200713
BuildRequires:  python3-django-appconf >= 1.0.3
BuildRequires:  python3-django-auth-ldap >= 1.3.0
BuildRequires:  python3-django-crispy-forms >= 1.9.0
BuildRequires:  python3-django-filter >= 2.4.0
BuildRequires:  python3-django-redis >= 4.11.0
BuildRequires:  python3-django_compressor >= 2.4
BuildRequires:  python3-djangorestframework >= 3.11
BuildRequires:  python3-filelock >= 3.7
BuildRequires:  python3-fluent
BuildRequires:  python3-gobject >= 3.34.0
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-gobject-cairo
BuildRequires:  python3-google-cloud-translate >= 3.0.0
BuildRequires:  python3-hiredis >= 1.0.1
BuildRequires:  python3-html2text >= 2019.8.11
BuildRequires:  python3-httpretty
BuildRequires:  python3-iniparse = 0.5
BuildRequires:  python3-jsonschema >= 4.5
BuildRequires:  python3-lxml >= 4.9.1
BuildRequires:  python3-misaka >= 2.1.0
BuildRequires:  python3-openpyxl >= 2.6.0
BuildRequires:  python3-packaging >= 20.5
BuildRequires:  python3-phply >= 1.2.5
BuildRequires:  python3-psycopg2 >= 2.7.7
BuildRequires:  python3-pyahocorasick >= 1.4
BuildRequires:  python3-pycairo >= 1.15.3
BuildRequires:  python3-pyicumessageformat >= 1.0.0
BuildRequires:  python3-pyparsing >= 3.0.7
BuildRequires:  python3-python-akismet >= 0.4.2
BuildRequires:  python3-python-dateutil >= 2.8.1
BuildRequires:  python3-python-redis-lock >= 3.6.0
BuildRequires:  python3-python3-saml >= 1.2.1
BuildRequires:  python3-pytz
BuildRequires:  python3-rapidfuzz >= 2.6.0
BuildRequires:  python3-requests >= 2.26.0
BuildRequires:  python3-responses >= 0.10.1
BuildRequires:  python3-ruamel.yaml >= 0.16.0
BuildRequires:  python3-selenium
BuildRequires:  python3-sentry-sdk >= 1.6
BuildRequires:  python3-setuptools >= 40.3.0
BuildRequires:  python3-siphashc >= 1.2
BuildRequires:  python3-social-auth-app-django >= 5.0.0
BuildRequires:  python3-social-auth-core >= 4.3.0
BuildRequires:  python3-sphinx-jsonschema
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-httpdomain
BuildRequires:  python3-tesserocr >= 2.3.0
BuildRequires:  python3-translation-finder >= 2.14
BuildRequires:  python3-user-agents >= 2.0
BuildRequires:  python3-weblate-language-data >= 2022.7
BuildRequires:  python3-weblate-schemas = 2022.1
BuildRequires:  python3-zeep >= 3.2.0
BuildRequires:  tesseract-ocr-traineddata-english
BuildRequires:  tesseract-ocr-traineddata-orientation_and_script_detection
BuildRequires:  translate-toolkit >= 3.7.2
BuildRequires:  typelib(Pango) >= 1.0
BuildRequires:  typelib(PangoCairo) >= 1.0
BuildRequires:  user(wwwrun)
Requires:       borgbackup >= 1.1.11
Requires:       cron
Requires:       git
Requires:       gpg2
Requires:       python3-Cython >= 0.29.14
Requires:       python3-Django >= 3.2
Requires:       python3-GitPython >= 2.1.15
Requires:       python3-Levenshtein
Requires:       python3-Pillow >= 9.0.0
Requires:       python3-Pygments >= 2.6.0
Requires:       python3-bleach >= 3.1.1
Requires:       python3-celery >= 5.0.3
Requires:       python3-charset-normalizer >= 2.0.12
Requires:       python3-cssselect >= 1.2
Requires:       python3-diff_match_patch = 20200713
Requires:       python3-django-appconf >= 1.0.3
Requires:       python3-django-crispy-forms >= 1.9.0
Requires:       python3-django-filter >= 2.4.0
Requires:       python3-django-redis >= 4.11.0
Requires:       python3-django_compressor >= 2.4
Requires:       python3-djangorestframework >= 3.11
Requires:       python3-filelock >= 3.7
Requires:       python3-fluent
Requires:       python3-gobject >= 3.34.0
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-hiredis >= 1.0.1
Requires:       python3-html2text >= 2019.8.11
Requires:       python3-jsonschema >= 4.5
Requires:       python3-lxml >= 4.9.1
Requires:       python3-misaka >= 2.1.0
Requires:       python3-openpyxl >= 2.6.0
Requires:       python3-packaging >= 20.5
Requires:       python3-pyahocorasick >= 1.4
Requires:       python3-pycairo >= 1.15.3
Requires:       python3-pyicumessageformat >= 1.0.0
Requires:       python3-pyparsing >= 3.0.7
Requires:       python3-python-dateutil >= 2.8.1
Requires:       python3-python-redis-lock >= 3.6.0
Requires:       python3-rapidfuzz >= 2.6.0
Requires:       python3-requests >= 2.26.0
Requires:       python3-sentry-sdk >= 1.6
Requires:       python3-setuptools >= 40.3.0
Requires:       python3-siphashc >= 1.2
Requires:       python3-social-auth-app-django >= 5.0.0
Requires:       python3-social-auth-core >= 4.3.0
Requires:       python3-translation-finder >= 2.14
Requires:       python3-user-agents >= 2.0
Requires:       python3-weblate-language-data >= 2022.7
Requires:       python3-weblate-schemas = 2022.1
Requires:       translate-toolkit >= 3.7.2
Requires:       ((apache2 and apache2-mod_wsgi) or (nginx and uwsgi))
Requires:       (postgresql and python3-psycopg2 >= 2.7.7 and postgresql-contrib)
Requires:       typelib(Pango) >= 1.0
Requires:       typelib(PangoCairo) >= 1.0
Requires(pre):  user(wwwrun)
Recommends:     borgbackup >= 1.1.9
Recommends:     git-review >= 1.27.0
Recommends:     git-svn
Recommends:     mercurial >= 5.2
Recommends:     python3-aeidon >= 1.9
Recommends:     python3-boto3 >= 1.15.0
# optional feature from aeidon is used
Recommends:     python3-chardet
Recommends:     python3-django-auth-ldap >= 1.3.0
Recommends:     python3-docutils
Recommends:     python3-google-cloud-translate >= 3.0.0
Recommends:     python3-iniparse = 0.5
Recommends:     python3-phply >= 1.2.5
Recommends:     python3-python-akismet >= 0.4.2
Recommends:     python3-python-memcached
Recommends:     python3-python3-saml >= 1.2.1
Recommends:     python3-pytz
Recommends:     python3-ruamel.yaml >= 0.16.0
Recommends:     python3-tesserocr >= 2.3.0
Recommends:     python3-zeep >= 3.2.0
Recommends:     tesseract-ocr-traineddata-english
Recommends:     tesseract-ocr-traineddata-orientation_and_script_detection
BuildArch:      noarch
ExcludeArch:    %{ix86}

%description
Weblate is a free web-based translation tool with tight version control
integration. It features simple and clean user interface, propagation of
translations across components, quality checks and automatic linking to source
files.

List of features includes:

* Easy web based translation
* Propagation of translations across components (for different branches)
* Tight git integration - every change is represented by Git commit
* Usage of Django's admin interface
* Upload and automatic merging of po files
* Links to source files for context
* Allows to use machine translation services
* Message quality checks
* Tunable access control
* Wide range of supported translation formats (Getext, Qt, Java, Windows, Symbian and more)

%package doc
Summary:        Weblate Documentation
BuildArch:      noarch

%description doc
HTML documentation files for the Weblate collaborative web translation tool.

%prep
%setup -q -n %{_name}-%{version}
%autopatch -p1

sed -i \
    -e 's:#!%{_bindir}/env python3:#!%{_bindir}/python3:' \
    setup.py manage.py
# do not pull in the diff match patch
sed -i -e '/diff-match-patch/d' requirements.txt
# do not hardcode versions
sed -e 's:==:>=:g' \
    -i requirements*.txt \
    -i setup.py

%build
%make_build -C docs html
rm docs/_build/html/.buildinfo
# Copy example settings
cp weblate/settings_example.py weblate/settings.py
# Set correct directories in settings
sed -i 's@^BASE_DIR = .*@BASE_DIR = "%{WLDIR}"@g' weblate/settings.py
sed -i 's@^DATA_DIR = .*@DATA_DIR = "%{WLDATADIR}"@g' weblate/settings.py
sed -i "s@%{_datadir}/weblate@%{WLDATADIR}@" weblate/examples/apache.conf

%install
install -d %{buildroot}/%{WLDIR}
install -d %{buildroot}/%{WLETCDIR}

# Copy all files
cp -a . %{buildroot}/%{WLDIR}
# Remove test data
rm -rf %{buildroot}/%{WLDIR}/data-test
# remove .git directory
rm -rf %{buildroot}/%{WLDIR}/.git

# We ship this separately
rm -rf %{buildroot}/%{WLDIR}/docs
rm -f %{buildroot}/%{WLDIR}/README.rst \
    %{buildroot}/%{WLDIR}/ChangeLog \
    %{buildroot}/%{WLDIR}/COPYING \
    %{buildroot}/%{WLDIR}/INSTALL \
    %{buildroot}/%{WLDIR}/BACKERS.rst \
    %{buildroot}/%{WLDIR}/CONTRIBUTING.md

# Byte compile python files
%py3_compile %{buildroot}/%{WLDIR}

# remove dupes
%fdupes %{buildroot}/%{WLDIR}

# Move configuration to etc
mv %{buildroot}/%{WLDIR}/weblate/settings.py %{buildroot}/%{WLETCDIR}/
ln -s %{WLETCDIR}/settings.py %{buildroot}/%{WLDIR}/weblate/settings.py

# Apache config
install -d %{buildroot}/%{_sysconfdir}/apache2/vhosts.d/
install -m 644 weblate/examples/apache.conf %{buildroot}/%{_sysconfdir}/apache2/vhosts.d/weblate.conf

# Whoosh index dir
install -d %{buildroot}/%{WLDATADIR}

%pre
if test -f %{WLDIR}/PKG-INFO ; then
 ln -f %{WLDIR}/PKG-INFO %{WLDIR}/PKG-INFO.old
fi

%post
if test -f %{WLDIR}/PKG-INFO.old ; then
 if ! cmp -s %{WLDIR}/PKG-INFO.old %{WLDIR}/PKG-INFO ; then
  echo "Performing version upgrade from `cat %{WLDIR}/PKG-INFO.old` to %{version}."
  echo "Please check https://docs.weblate.org/en/latest/admin/upgrade.html for additional steps to upgrade."
 fi
 rm %{WLDIR}/PKG-INFO.old
fi
# Static files
# add || : as the tansaction fails in OBS because it needs running redis/pgsql databases
su - wwwrun -s /bin/bash -c '%{WLDIR}/manage.py collectstatic --noinput' || :

%check
# first make sure we use buildroot properly
sed -i 's@^BASE_DIR = .*@BASE_DIR = "%{buildroot}%{WLDIR}"@g' weblate/settings.py
sed -i 's@^DATA_DIR = .*@DATA_DIR = "%{buildroot}%{WLDATADIR}"@g' weblate/settings.py

export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
export DJANGO_SETTINGS_MODULE=weblate.settings_test

# start the redis server
%{_sbindir}/redis-server &

# PostgreSQL test databse setup
export CI_DB_USER=`id -un`
export CI_DATABASE=postgresql
export CI_DB_HOST=/tmp
export PGDATA=$(mktemp -d)
%{_bindir}/pg_ctl -l postgresql.log initdb
%{_bindir}/pg_ctl -l postgresql.log -o "--unix_socket_directories=/tmp" start

# Collect static files for testsuite
python3 ./manage.py collectstatic --noinput -v 2
python3 ./manage.py compilemessages -v 2
# Run the testsuite
python3 ./manage.py check -v 2
python3 ./manage.py test -v 2

# kill the redis server
pkill -f redis-server

# Cleanup postgresql
%{_bindir}/pg_ctl stop
rm -r $PGDATA

%files
%license COPYING
%doc README.rst
%config(noreplace) %{_sysconfdir}/weblate
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/vhosts.d
%config(noreplace) %{_sysconfdir}/apache2/vhosts.d/weblate.conf
%{WLDIR}
%attr(0755,wwwrun,www) %{WLDATADIR}

%files doc
%doc docs/_build/html

%changelog
