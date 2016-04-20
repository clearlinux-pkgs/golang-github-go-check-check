#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-go-check-check
Version  : 4f90aeace3a26ad7021961c297b22c42160c7b25
Release  : 1
URL      : https://github.com/go-check/check/archive/4f90aeace3a26ad7021961c297b22c42160c7b25.tar.gz
Source0  : https://github.com/go-check/check/archive/4f90aeace3a26ad7021961c297b22c42160c7b25.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : go

%description
Instructions
============
Install the package with:
go get gopkg.in/check.v1

Import it with:

%prep
%setup -q -n check-4f90aeace3a26ad7021961c297b22c42160c7b25

%build

%install
gopath="/usr/lib/golang"
library_path="gopkg.in/check.v1"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x gopkg.in/check.v1

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/gopkg.in/check.v1/benchmark.go
/usr/lib/golang/src/gopkg.in/check.v1/benchmark_test.go
/usr/lib/golang/src/gopkg.in/check.v1/bootstrap_test.go
/usr/lib/golang/src/gopkg.in/check.v1/check.go
/usr/lib/golang/src/gopkg.in/check.v1/check_test.go
/usr/lib/golang/src/gopkg.in/check.v1/checkers.go
/usr/lib/golang/src/gopkg.in/check.v1/checkers_test.go
/usr/lib/golang/src/gopkg.in/check.v1/export_test.go
/usr/lib/golang/src/gopkg.in/check.v1/fixture_test.go
/usr/lib/golang/src/gopkg.in/check.v1/foundation_test.go
/usr/lib/golang/src/gopkg.in/check.v1/helpers.go
/usr/lib/golang/src/gopkg.in/check.v1/helpers_test.go
/usr/lib/golang/src/gopkg.in/check.v1/printer.go
/usr/lib/golang/src/gopkg.in/check.v1/printer_test.go
/usr/lib/golang/src/gopkg.in/check.v1/reporter.go
/usr/lib/golang/src/gopkg.in/check.v1/reporter_test.go
/usr/lib/golang/src/gopkg.in/check.v1/run.go
/usr/lib/golang/src/gopkg.in/check.v1/run_test.go
