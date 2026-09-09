#
# spec file for package python-sqlite-vec
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-sqlite-vec
Version:        0.1.9
Release:        0
Summary:        Vector search SQLite extension for Python
# Dual-licensed by upstream (LICENSE-MIT + LICENSE-APACHE); licensee picks one.
License:        Apache-2.0 OR MIT
URL:            https://github.com/asg017/sqlite-vec
# PyPI 0.1.9 is wheels-only (no sdist). Use the GitHub tag archive.
Source0:        https://github.com/asg017/sqlite-vec/archive/refs/tags/v%{version}.tar.gz#/sqlite-vec-%{version}.tar.gz
# Distro-only pyproject: upstream has no Python build (sqlite-dist emits wheels).
Source1:        pyproject.toml
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(sqlite3)
%python_subpackages

%description
sqlite-vec is a small SQLite extension for storing and querying float,
int8, and binary vectors in vec0 virtual tables. This package ships the
loadable (vec0.so) plus Python helpers to load it into sqlite3
connections and to serialize vectors.

%prep
%autosetup -p1 -n sqlite-vec-%{version}
cp %{SOURCE1} pyproject.toml
sed -i 's/^version = ".*"/version = "%{version}"/' pyproject.toml

%build
# sqlite-vec.h is generated; DATE/SOURCE are informational (vec_debug()).
# sed instead of envsubst: BR envsubst conflicts with envsubst-mini in the
# gettext-runtime-mini buildroot.
VERSION="$(cat VERSION)"
DATE="$(date -u -r VERSION +'%%FT%%TZ%%z')"
SOURCE="v%{version}"
VERSION_MAJOR="$(echo "$VERSION" | cut -d. -f1)"
VERSION_MINOR="$(echo "$VERSION" | cut -d. -f2)"
VERSION_PATCH="$(echo "$VERSION" | cut -d. -f3 | cut -d- -f1)"
sed -e 's/${VERSION_MAJOR}/'"$VERSION_MAJOR"'/g' \
    -e 's/${VERSION_MINOR}/'"$VERSION_MINOR"'/g' \
    -e 's/${VERSION_PATCH}/'"$VERSION_PATCH"'/g' \
    -e 's/${VERSION}/'"$VERSION"'/g' \
    -e 's/${DATE}/'"$DATE"'/g' \
    -e 's/${SOURCE}/'"$SOURCE"'/g' \
    sqlite-vec.h.tmpl > sqlite-vec.h

# Loadable only: system sqlite headers, no vendor/sqlite3.c, no static .a.
# -lm after the source so sqrt/sqrtf resolve (upstream Makefile does this
# on Linux; the PyPI wheel leaves them undefined).
mkdir -p dist
gcc %{optflags} %{?build_ldflags} -fPIC -shared \
  $(pkg-config --cflags sqlite3) \
  sqlite-vec.c -o dist/vec0.so -lm
chmod 0755 dist/vec0.so

# Recreate the PyPI wheel layout: sqlite_vec/{__init__.py,vec0.so}.
mkdir -p sqlite_vec
cp -p dist/vec0.so sqlite_vec/vec0.so
cat > sqlite_vec/__init__.py << 'PY'
from os import path
import sqlite3

__version__ = "@VERSION@"
__version_info__ = tuple(__version__.split("."))

def loadable_path():
  """ Returns the full path to the sqlite-vec loadable SQLite extension bundled with this package """

  loadable_path = path.join(path.dirname(__file__), "vec0")
  return path.normpath(loadable_path)

def load(conn: sqlite3.Connection)  -> None:
  """ Load the sqlite-vec SQLite extension into the given database connection. """

  conn.load_extension(loadable_path())
PY
sed -i 's/@VERSION@/%{version}/' sqlite_vec/__init__.py
cat bindings/python/extra_init.py >> sqlite_vec/__init__.py

# Force an archful wheel so vec0.so lands in sitearch, not sitelib.
cat > setup.py << 'PY'
from setuptools import setup
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


setup(distclass=BinaryDistribution)
PY

%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/sqlite_vec
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Smoke the packaged API (import + load_extension + vec_version).
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B -c 'import sqlite3, sqlite_vec; db = sqlite3.connect(":memory:"); db.enable_load_extension(True); sqlite_vec.load(db); ver = db.execute("select vec_version()").fetchone()[0]; assert ver.startswith("v"), ver; print("vec_version", ver)'
# Upstream loadable suite (needs numpy). dist/vec0.so is the same binary.
# 32-bit: size_t/limit tests overflow (expected 1, found 429496729601).
%ifnarch %{ix86} %{arm}
%pytest_arch tests/test-loadable.py
%endif

%files %{python_files}
%doc README.md ARCHITECTURE.md
%license LICENSE-MIT LICENSE-APACHE
%{python_sitearch}/sqlite_vec
%{python_sitearch}/sqlite_vec-%{version}.dist-info

%changelog
