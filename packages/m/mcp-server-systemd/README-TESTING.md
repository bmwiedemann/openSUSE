There are two different type of test available upstream:
1. Unit tests run with `go test` and can be excuted in bats with `./test/unit-tests.bat`
2.1 Intregrated conteneraized tests which are intergrated tests so that the different features 
    are tested agains a running systemd and not just a mock one. This tests can be run with
    `./test/integrated-tests.bat`
2.2 In order to check authentication workflows there are `./tests/keycloak-tests.bat` which spawn
    an additional keycloack container for authorization
