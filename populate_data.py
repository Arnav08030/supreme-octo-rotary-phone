import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project2.settings')
django.setup()

from app2.models import country, states, districts

def populate():
    # Define sample data
    # format: { country_name: { state_name: [district1, district2, ...] } }
    data = {
        'India': {
            'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Thane'],
            'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore', 'Belgaum'],
            'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Trichy', 'Salem'],
            'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar'],
            'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Ajmer']
        },
        'USA': {
            'California': ['Los Angeles', 'San Francisco', 'San Diego', 'San Jose', 'Fresno'],
            'Texas': ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth'],
            'Florida': ['Miami', 'Tampa', 'Orlando', 'Jacksonville', 'Tallahassee'],
            'New York': ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse'],
            'Illinois': ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville']
        }
    }

    print("Populating database...")

    for c_name, states_data in data.items():
        # Get or create country
        c_obj, created = country.objects.get_or_create(country=c_name)
        if created:
            print(f"Created country: {c_name}")
        else:
            print(f"Country exists: {c_name}")

        for s_name, districts_list in states_data.items():
            # Get or create state
            s_obj, created = states.objects.get_or_create(country=c_obj, state=s_name)
            if created:
                print(f"  Created state: {s_name}")
            else:
                print(f"  State exists: {s_name}")

            for d_name in districts_list:
                # Get or create district
                d_obj, created = districts.objects.get_or_create(state=s_obj, district=d_name)
                if created:
                    print(f"    Created district: {d_name}")
                else:
                    print(f"    District exists: {d_name}")

    print("Population complete.")

if __name__ == "__main__":
    populate()
