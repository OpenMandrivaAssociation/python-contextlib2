%define modname contextlib2

Name:               python-contextlib2
Version:            0.5.0
Release:            1
Summary:            Backports and enhancements for the contextlib module
Group:              Development/Python
License:            Python
URL:                http://pypi.python.org/pypi/contextlib2
Source0:            https://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:          noarch
BuildRequires:      python-devel
BuildRequires:	python-setuptools

%description
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

%prep
%setup -q -n %{modname}-%{version}

sed -i 's/unittest2/unittest/' test_contextlib2.py

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root=%{buildroot}

%check
#python test_contextlib2.py

%files
%doc README.md VERSION.txt NEWS.rst LICENSE.txt
%{py_puresitedir}/%{modname}.py*
%{py_puresitedir}/%{modname}-%{version}*

