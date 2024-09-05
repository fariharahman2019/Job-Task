class Client:
    def __init__(self, name, reviews, payment_verified, location, hire_rate, jobs_posted, open_jobs, money_spent, hourly_rate, total_hours):
        self.name = name
        self.reviews = reviews
        self.payment_verified = payment_verified  #boolean
        self.location = location
        self.hire_rate = hire_rate
        self.jobs_posted = jobs_posted
        self.open_jobs = open_jobs
        self.money_spent = money_spent
        self.hourly_rate = hourly_rate
        self.total_hours = total_hours

    def avg_review_score(self):
        return sum(self.reviews) / len(self.reviews) if self.reviews else 0

    def should_approach(self):
        # Condition 1: Hourly rate at least $25
        if self.hourly_rate < 25:
            return False
        
        # Condition 2: Hire rate not lower than 40%
        if self.hire_rate < 40:
            return False
        
        # Condition 3: Average review score must be at least 4.0 (assuming review scale of 1 to 5)
        if self.avg_review_score() < 4:
            return False
        
        # Condition 4: Client has spent at least $10k
        if self.money_spent < 10000:
            return False
        
        # Preferred Condition: Clients spending above $50k or $100k are prioritized
        if self.money_spent >= 50000:
            print(f"Client {self.name} is a high spender with ${self.money_spent} spent. Priority!")
        
        return True

    def display_info(self):
        print(f"Client: {self.name}")
        print(f"Reviews: {self.reviews}")
        print(f"Payment Verified: {self.payment_verified}")
        print(f"Location: {self.location}")
        print(f"Hire Rate: {self.hire_rate}%")
        print(f"Jobs Posted: {self.jobs_posted}")
        print(f"Open Jobs: {self.open_jobs}")
        print(f"Total Money Spent: ${self.money_spent}")
        print(f"Hourly Rate Paid: ${self.hourly_rate}/hr")
        print(f"Total Hours Worked: {self.total_hours} hours")
        print(f"Average Review Score: {self.avg_review_score()}")

# Example Clients
client1 = Client(
    name="John Doe",
    reviews=[5, 4, 5, 4.5],
    payment_verified=True,
    location="USA",
    hire_rate=50,
    jobs_posted=10,
    open_jobs=2,
    money_spent=60000,
    hourly_rate=30,
    total_hours=1200
)

client2 = Client(
    name="Jane Smith",
    reviews=[3.5, 4, 4.5, 4],
    payment_verified=False,
    location="Canada",
    hire_rate=30,
    jobs_posted=15,
    open_jobs=5,
    money_spent=8000,
    hourly_rate=20,
    total_hours=800
)

for client in [client1, client2]:
    client.display_info()
    if client.should_approach():
        print(f"Approach {client.name} for a job!\n")
    else:
        print(f"Do not approach {client.name} for a job.\n")
