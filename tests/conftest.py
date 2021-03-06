import pytest
import os
import json

#
# JSON schema and test data loading fixtures
#
@pytest.fixture
def test_dir():
    return os.path.dirname(__file__)


@pytest.fixture
def data_dir(test_dir):
    return os.path.join(test_dir, 'data')


@pytest.fixture
def jsonschema_dir(test_dir):
    return os.path.join(test_dir, '..', 'jsonschema')


@pytest.fixture
def zenodo_examples_data_dir(request):
    """Return the directory of the currently running test script"""
    return request.fspath.join('../../examples/zenodo-v1/data')


def load_schema(basedir, filename):
    with open(os.path.join(basedir, filename)) as fp:
        schema = json.load(fp)
    return schema


@pytest.fixture
def relation_schema(jsonschema_dir):
    return load_schema(jsonschema_dir, 'relation.json')


@pytest.fixture
def object_schema(jsonschema_dir):
    return load_schema(jsonschema_dir, 'object.json')


@pytest.fixture
def event_schema(jsonschema_dir):
    return load_schema(jsonschema_dir, 'event.json')


#
# Payload and events mocks loading (form JSON files)
#
@pytest.fixture
def zenodo_relation_events_dir():
    pass


#
# Raw relation payload and events examples
#
@pytest.fixture
def ads_relation_payloads():
    # Example from ADS
    data = [
        {
            "relationship_type": {
                "original_relationship_schema": "DataCite",
                "original_relationship_name": "Cites",
                "scholix_relationship": "References"
            },
            "target": {
                "Identifier": {
                    "id": "10.5281/zenodo.11020",
                    "id_schema": "DOI",
                    "id_url": "https://doi.org"
                },
                "type": {
                    "name": "software"
                }
            },
            "source": {
                "identifier": {
                    "id": "2016ApJ...818..156C",
                    "id_schema": "bibcode",
                    "id_url": "http://adsabs.harvard.edu/abs/"
                }
            },
            "license_url": "https://creativecommons.org/publicdomain/zero/1.0/"
        },
    ]

    return data


@pytest.fixture()
def ads_relation_events():
    # Two events that are described in ADS-mock-events.md
    data = [
        {
          "time": "1441166640.359496",
          "id": "d969a56d-e520-405d-a24f-497ac6923781",
          "creator": "ADS",
          "payload": [
            {
              "source": {
                "identifier": {
                  "id_url": "http://adsabs.harvard.edu/abs/",
                  "id": "2016ApJ...818..156C",
                  "id_schema": "bibcode"
                }
              },
              "relationship_type": {
                "scholix_relationship": "References",
                "original_relationship_name": "Cites",
                "original_relationship_schema": "DataCite"
              },
              "target": {
                "type": {
                  "name": "software"
                },
                "identifier": {
                  "id_url": "https://doi.org",
                  "id": "10.5281/zenodo.11020",
                  "id_schema": "DOI"
                }
              },
              "license_url": "https://creativecommons.org/"
                             "publicdomain/zero/1.0/"
            }
          ],
          "source": "ADS.Discovery",
          "description": "ADS citation events",
          "event_type": "relation_created"
        },
        {
          "time": "1441166640.359496",
          "id": "d969a56d-e520-405d-a24f-497ac6923781",
          "creator": "ADS",
          "payload": [
            {
              "source": {
                "identifier": {
                  "id_url": "http://adsabs.harvard.edu/abs/",
                  "id": "2016zen.soft123456X",
                  "id_schema": "bibcode"
                }
              },
              "relationship_type": {
                "original_relationship_name": "IsIdenticalTo",
                "original_relationship_schema": "DataCite"
              },
              "target": {
                "type": {
                  "name": "software"
                },
                "identifier": {
                  "id_url": "https://doi.org",
                  "id": "10.5281/zenodo.11020",
                  "id_schema": "DOI"
                }
              },
              "license_url": "https://creativecommons.org/"
                             "publicdomain/zero/1.0/"
            }
          ],
          "source": "ADS.Discovery",
          "description": "ADS citation events",
          "event_type": "relation_created"
        }
    ]
    return data


#
# Raw object events and payload fixtures
#
@pytest.fixture()
def zenodo_object_events():
    """Example object events from Zenodo."""
    # Two events that are described in ADS-mock-events.md
    data = [
        {
          "time": "1441166640.359496",
          "id": "d969a56d-e520-405d-a24f-497ac6923781",
          "creator": "Zenodo",
          "payload": [
            {
              "object_publication_date": "2014-06-24",
              "object_provider": {
                "name": "Zenodo"
              },
              "object": {
                "identifier": {
                  "id_url": "https://doi.org",
                  "id": "10.5281/zenodo.11020",
                  "id_schema": "DOI"
                }
              }
            }
          ],
          "source": "Zenodo.System",
          "event_type": "object_created"
        },
    ]
    return data



