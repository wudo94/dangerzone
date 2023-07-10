# Dangerzone Testing

Dangerzone has some automated testing under `tests/`.

The following assumes that you have already setup the development environment.

## Run tests

Unit / integration tests are run with:

```bash
poetry run make test
```

## Run large tests

We also have a larger set of tests that can take a day or more to run, where we evaluate the completeness of Dangerzone conversions.

```bash
poetry run make large-test
```

### Test report generation

There are two kinds of reports produced: junit report, test analysis report.

The Junit report is stored under `tests/test_docs_large/results/junit/` and it is composed of the JUnit XML file describing the pytest run.

The second kind of report is used to analyze the errors generated during the conversion. It can only be done after test training. It is obtained by running:

```bash
cd tests/docs_test_large
make report
```

### Updating large tests

The goal of these tests is to compare the current code revision with a past one and make sure there are no regressions

