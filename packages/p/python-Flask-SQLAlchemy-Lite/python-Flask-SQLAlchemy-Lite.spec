#
# spec file for package python-Flask-SQLAlchemy-Lite
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-Flask-SQLAlchemy-Lite
Version:        0.2.1
Release:        0
Summary:        Integrate SQLAlchemy with Flask
License:        MIT
URL:            https://github.com/pallets-eco/flask-sqlalchemy-lite
Source:         https://github.com/pallets-eco/flask-sqlalchemy-lite/archive/refs/tags/%{version}.tar.gz#/flask_sqlalchemy_lite-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module flit-core >= 3}
BuildRequires:  fdupes
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module Flask >= 3.0}
BuildRequires:  %{python_module asgiref >= 3.2}
BuildRequires:  %{python_module greenlet >= 1}
BuildRequires:  %{python_module SQLAlchemy >= 2.0.31}
# /SECTION
Requires:       python-Flask >= 3.0
# Flask[async]
Requires:       python-asgiref >= 3.2
Requires:       python-SQLAlchemy >= 2.0.31
# SQLAlchemy[asyncio]
Requires:       python-greenlet >= 1.0
# Provide the lowercase name too
Provides:       python-flask-sqlalchemy-lite = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Integrate SQLAlchemy with Flask. Use Flask's config to define SQLAlchemy
database engines. Create SQLAlchemy ORM sessions that are cleaned up
automatically after requests.

Intended to be a replacement for Flask-SQLAlchemy. Unlike the prior extension,
this one does not attempt to manage the model base class, tables, metadata, or
multiple binds for sessions. This makes the extension much simpler, letting the
developer use standard SQLAlchemy instead.

%prep
%autosetup -p1 -n flask-sqlalchemy-lite-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/flask_sqlalchemy_lite
%{python_sitelib}/flask_sqlalchemy_lite-%{version}.dist-info

%changelog
