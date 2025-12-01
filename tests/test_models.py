import pytest
from django.utils import timezone
from climate.models import Community, ClimateRecord

@pytest.mark.django_db
def test_create_community_and_record():
    c = Community.objects.create(name="TestTown", borough="TestB", latitude=40.0, longitude=-74.0)
    r = ClimateRecord.objects.create(community=c, date=timezone.now().date(), temperature=12.3, precipitation=0.1, pollution_index=45)
    assert c.records.count() == 1
    assert r.temperature == 12.3
