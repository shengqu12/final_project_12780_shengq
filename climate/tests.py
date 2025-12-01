from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from .models import CommunityGeo, ClimateRiskFactor

@pytest.mark.django_db
def test_dashboard_view(client):
    community = CommunityGeo.objects.create(
        community_id='C1',
        community_name='Test Community',
        latitude=40.0,
        longitude=-74.0
    )

    ClimateRiskFactor.objects.create(
        community_id=community,
        date='2024-01-01',
        annual_high_temp_days=5,
        flood_risk_score=0.1,
        storm_risk_score=0.2,
        heat_health_risk_coeff=0.3,
        year=2024,
        month=1
    )

    url = reverse('climate:dashboard')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Test Community' in str(response.content)
