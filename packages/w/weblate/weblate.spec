#
# spec file for package weblate
#
# Copyright (c) 2025 SUSE LLC
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
Name:           weblate
Version:        5.9.2
Release:        0
Summary:        Web-based translation tool
License:        GPL-3.0-or-later
URL:            https://github.com/WeblateOrg/weblate
Source0:        https://github.com/WeblateOrg/weblate/releases/download/weblate-%{version}/weblate-%{version}.tar.gz
Source1:        https://github.com/WeblateOrg/weblate/releases/download/weblate-%{version}/weblate-%{version}.tar.gz.sigstore.json
# GPG key from Michal Čihař
# Fingerprint 63CB 1DF1 EF12 CF2A C0EE 5A32 9C27 B313 42B7 511D
# https://cihar.com/.well-known/openpgpkey/hu/wmxth3chu9jfxdxywj1skpmhsj311mzm
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE skip-test_ocr.patch gh#WeblateOrg/weblate#8931 mcepl@suse.com, mmachova@suse.com
# skip failing test_ocr and test_ocr_backend
# most probably some issue on our side
Patch:          skip-test_ocr.patch
# PATCH-FIX-UPSTREAM https://github.com/WeblateOrg/weblate/commit/c59bec99e84abc21b225b235cfec719d32847787 fix(formats): use new more tolerant ttkit
Patch:          ttkit.patch
BuildRequires:  bitstream-vera
BuildRequires:  borgbackup >= 1.2.5
BuildRequires:  fdupes
BuildRequires:  git >= 2.28
BuildRequires:  git-review >= 1.27.0
BuildRequires:  git-svn
BuildRequires:  gpg2
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  mercurial >= 6.2
BuildRequires:  openssh
BuildRequires:  postgresql
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython >= 3.0.0
BuildRequires:  python3-Django >= 5.0
BuildRequires:  python3-GitPython >= 3.1.0
BuildRequires:  python3-Pillow >= 10.3.0
BuildRequires:  python3-Pygments >= 2.17.0
BuildRequires:  python3-Unidecode >= 1.3.8
BuildRequires:  python3-aeidon >= 1.14.1
BuildRequires:  python3-ahocorasick-rs >= 0.20.0
BuildRequires:  python3-aliyun-python-sdk-alimt >= 3.2.0
BuildRequires:  python3-altcha >= 0.1.7
BuildRequires:  python3-boto3 >= 1.28.62
BuildRequires:  python3-celery >= 5.4.0
BuildRequires:  python3-certifi >= 2024.8.30
BuildRequires:  python3-charset-normalizer >= 2.0.12
BuildRequires:  python3-crispy-bootstrap3 >= 2024.1
BuildRequires:  python3-cryptography >= 42.0.4
BuildRequires:  python3-cssselect >= 1.2
BuildRequires:  python3-cyrtranslit >= 1.1.0
BuildRequires:  python3-dateparser >= 1.2.0
BuildRequires:  python3-diff_match_patch = 20241021
BuildRequires:  python3-django-appconf >= 1.0.3
BuildRequires:  python3-django-auth-ldap >= 4.6.0
BuildRequires:  python3-django-celery-beat >= 2.6.0
BuildRequires:  python3-django-cors-headers >= 4.3.0
BuildRequires:  python3-django-crispy-forms >= 2.3
BuildRequires:  python3-django-filter >= 23.4
BuildRequires:  python3-django-otp >= 1.5.2
BuildRequires:  python3-django-otp-webauthn >= 0.4.0
BuildRequires:  python3-django-redis >= 5.4.0
BuildRequires:  python3-django_compressor >= 4.4
BuildRequires:  python3-djangorestframework >= 3.15.2
BuildRequires:  python3-drf-spectacular >= 0.27.2
BuildRequires:  python3-drf-spectacular-sidecar
BuildRequires:  python3-filelock >= 3.16.1
BuildRequires:  python3-fluent.syntax >= 0.18.1
BuildRequires:  python3-gobject >= 3.40.1
BuildRequires:  python3-google-cloud-storage >= 2.18.2
BuildRequires:  python3-google-cloud-translate >= 3.13.0
BuildRequires:  python3-hiredis >= 2.2.1
BuildRequires:  python3-html2text >= 2024.2.25
BuildRequires:  python3-iniparse >= 0.5
BuildRequires:  python3-jsonschema >= 4.23.0
BuildRequires:  python3-lxml >= 5.2.0
BuildRequires:  python3-mistletoe >= 1.4.0
BuildRequires:  python3-nh3 >= 0.2.14
BuildRequires:  python3-openai >= 1.3.0
BuildRequires:  python3-openpyxl >= 3.1.0
BuildRequires:  python3-packaging >= 23
BuildRequires:  python3-phply >= 1.2.6
BuildRequires:  python3-psycopg >= 3.1.8
BuildRequires:  python3-pycairo >= 1.20.0
BuildRequires:  python3-pyicumessageformat >= 1.0.0
BuildRequires:  python3-pyparsing >= 3.1.1
BuildRequires:  python3-python-akismet >= 0.4.2
BuildRequires:  python3-python-dateutil >= 2.8.2
BuildRequires:  python3-python-redis-lock >= 4
BuildRequires:  python3-python3-saml >= 1.2.1
BuildRequires:  python3-qrcode >= 7.4.1
BuildRequires:  python3-rapidfuzz >= 3.8.0
BuildRequires:  python3-redis >= 5.0.2
BuildRequires:  python3-requests >= 2.32.2
BuildRequires:  python3-responses >= 0.10.1
BuildRequires:  python3-respx >= 0.20.2
BuildRequires:  python3-ruamel.yaml >= 0.17.2
BuildRequires:  python3-selenium
BuildRequires:  python3-sentry-sdk >= 2.15.0
BuildRequires:  python3-setuptools >= 40.3.0
BuildRequires:  python3-siphashc >= 2.1
BuildRequires:  python3-social-auth-app-django >= 5.4.1
BuildRequires:  python3-social-auth-core >= 4.5.0
BuildRequires:  python3-tesserocr >= 2.6.1
BuildRequires:  python3-translation-finder >= 2.18
BuildRequires:  python3-user-agents >= 2.0
BuildRequires:  python3-weblate-language-data >= 2024.14
BuildRequires:  python3-weblate-schemas = 2024.2
BuildRequires:  tesseract-ocr-traineddata-english
BuildRequires:  tesseract-ocr-traineddata-orientation_and_script_detection
BuildRequires:  translate-toolkit >= 3.14.4
BuildRequires:  typelib(Pango) >= 1.0
BuildRequires:  typelib(PangoCairo) >= 1.0
BuildRequires:  typelib(Rsvg)
BuildRequires:  user(wwwrun)
Requires:       borgbackup >= 1.2.5
Requires:       cron
Requires:       git >= 2.28
Requires:       gpg2
Requires:       postgresql
Requires:       postgresql-contrib
Requires:       python3-Cython >= 3.0.0
Requires:       python3-Django >= 5.0
Requires:       python3-GitPython >= 3.1.0
Requires:       python3-Levenshtein
Requires:       python3-Pillow >= 10.3.0
Requires:       python3-Pygments >= 2.17.0
Requires:       python3-Unidecode >= 1.3.8
Requires:       python3-aeidon >= 1.14.1
Requires:       python3-ahocorasick-rs >= 0.20.0
Requires:       python3-altcha >= 0.1.7
Requires:       python3-celery >= 5.4.0
Requires:       python3-certifi >= 2024.8.30
Requires:       python3-charset-normalizer >= 2.0.12
Requires:       python3-crispy-bootstrap3 >= 2024.1
Requires:       python3-cryptography >= 42.0.4
Requires:       python3-cssselect >= 1.2
Requires:       python3-cyrtranslit >= 1.1.0
Requires:       python3-dateparser >= 1.2.0
Requires:       python3-diff_match_patch = 20241021
Requires:       python3-django-appconf >= 1.0.3
Requires:       python3-django-celery-beat >= 2.6.0
Requires:       python3-django-cors-headers >= 4.3.0
Requires:       python3-django-crispy-forms >= 2.3
Requires:       python3-django-filter >= 23.4
Requires:       python3-django-otp >= 1.5.2
Requires:       python3-django-otp-webauthn >= 0.4.0
Requires:       python3-django-redis >= 5.4.0
Requires:       python3-django_compressor >= 4.4
Requires:       python3-djangorestframework >= 3.15.2
Requires:       python3-drf-spectacular >= 0.27.2
Requires:       python3-drf-spectacular-sidecar
Requires:       python3-filelock >= 3.16.1
Requires:       python3-fluent.syntax >= 0.18.1
Requires:       python3-gobject >= 3.40.1
Requires:       python3-hiredis >= 2.2.1
Requires:       python3-html2text >= 2019.8.11
Requires:       python3-iniparse >= 0.5
Requires:       python3-jsonschema >= 4.23.0
Requires:       python3-lxml >= 5.2
Requires:       python3-mistletoe >= 1.4.0
Requires:       python3-nh3 >= 0.2.14
Requires:       python3-openpyxl >= 3.1.0
Requires:       python3-packaging >= 23
Requires:       python3-phply >= 1.2.6
Requires:       python3-pycairo >= 1.20.0
Requires:       python3-pyicumessageformat >= 1.0.0
Requires:       python3-pyparsing >= 3.1.1
Requires:       python3-python-dateutil >= 2.8.2
Requires:       python3-python-redis-lock >= 4
Requires:       python3-qrcode >= 7.4.1
Requires:       python3-rapidfuzz >= 3.8.0
Requires:       python3-redis >= 5.0.2
Requires:       python3-requests >= 2.32.2
Requires:       python3-ruamel.yaml >= 0.17.2
Requires:       python3-sentry-sdk >= 2.15.0
Requires:       python3-siphashc >= 2.1
Requires:       python3-social-auth-app-django >= 5.4.1
Requires:       python3-social-auth-core >= 4.5.0
Requires:       python3-tesserocr >= 2.6.1
Requires:       python3-translation-finder >= 2.18
Requires:       python3-user-agents >= 2.0
Requires:       python3-weblate-language-data >= 2024.14
Requires:       python3-weblate-schemas = 2024.2
Requires:       translate-toolkit >= 3.14.4
Requires:       ((apache2 and apache2-mod_wsgi) or (nginx and uwsgi))
Requires:       typelib(Pango) >= 1.0
Requires:       typelib(PangoCairo) >= 1.0
Requires(pre):  user(wwwrun)
Recommends:     git-review >= 1.27.0
Recommends:     git-svn
Recommends:     mercurial >= 6.2
Recommends:     python3-boto3 >= 1.25.0
Recommends:     python3-django-auth-ldap >= 1.3.0
Recommends:     python3-google-cloud-translate >= 3.8.0
Recommends:     python3-python-akismet >= 0.4.2
Recommends:     python3-python3-saml >= 1.2.1
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

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

sed -i \
    -e "s:#!%{_bindir}/env python3:#!%{_bindir}/python%{python3_bin_suffix}:" \
    setup.py manage.py \
    weblate/utils/generate_secret_key.py
sed -e 's:==:>=:g' \
    -i pyproject.toml

%build
# docs were dropped from the release tarball
#%%make_build -C docs html
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
timeout 5m %{_sbindir}/redis-server &

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

# Cleanup postgresql
%{_bindir}/pg_ctl stop
rm -r $PGDATA

# kill the redis server
# ... but as pkill returns 1 on a success, exit 0 instead
pkill -f redis-server || exit 0

%files
%license COPYING
%doc README.rst
%config(noreplace) %{_sysconfdir}/weblate
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/vhosts.d
%config(noreplace) %{_sysconfdir}/apache2/vhosts.d/weblate.conf
%{WLDIR}
%attr(0755,wwwrun,www) %{WLDATADIR}

%changelog
