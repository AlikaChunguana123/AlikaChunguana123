// SproutWise sector knowledge base.
// Used by the app for offline advice and sent to the server so the AI tailors its answer.
// Add a sector by copying one block; keep tips concrete and low-cost first.
window.SECTORS = {
  retail: {
    name: "Retail shop & market stall", icon: "🛍️",
    ideas: ["Bundle slow sellers with best sellers as a 'value pack'", "Start WhatsApp/Instagram ordering with local delivery or pickup", "Add a small, high-margin impulse rack near the till", "Offer pre-orders for seasonal items (school, holidays, festivals)"],
    marketing: ["Post 3 product photos a week with prices, since clear prices increase messages", "Loyalty card: buy 9, get the 10th free", "Partner with a nearby non-competing shop for cross-promotion", "Ask happy customers for Google/Facebook reviews and print a QR code at the till"],
    money: ["Track the top 20 products by profit, not just sales", "Negotiate payment terms (30 days) with suppliers once you're a regular buyer", "Count stock weekly and find what doesn't move in 60 days, then discount it", "Keep business and personal money in separate accounts"],
    risks: ["Overstocking cash into slow items", "Theft/shrinkage: do simple daily cash reconciliation", "Price wars with bigger stores: compete on service and convenience instead"]
  },
  food: {
    name: "Food, café & restaurant", icon: "🍲",
    ideas: ["Lunch combo at a fixed price for nearby offices", "Sell your signature sauce/snack packaged for take-home", "Catering for small events and meetings", "Pre-order meal boxes for the week"],
    marketing: ["Short videos of food being prepared get the most reach", "Register on local delivery apps, but push repeat customers to direct ordering", "'Dish of the week' to create urgency", "Collect phone numbers for a broadcast list (with permission)"],
    money: ["Cost every dish: food cost should be ~28–35% of the menu price", "Reduce waste: track what is thrown away daily", "Cut menu items that sell little and need special ingredients", "Buy staples in bulk with another small restaurant"],
    risks: ["Food safety and hygiene inspections, so keep a cleaning log", "Rising ingredient prices: review prices every quarter", "Staff turnover: train with simple written recipes"]
  },
  beauty: {
    name: "Beauty, salon & barber", icon: "💇",
    ideas: ["Membership: monthly fee for set services", "Sell aftercare products (high margin)", "Bridal/event packages with home visits", "Off-peak discounts on slow weekdays"],
    marketing: ["Before/after photos (with consent) on Instagram & TikTok", "Referral reward: both friends get 10–20% off", "Online booking link in your bio and on Google Maps", "Collaborate with local photographers and event planners"],
    money: ["Track revenue per chair/hour", "Charge a small deposit to reduce no-shows", "Commission + base for staff to motivate selling products", "Raise prices slightly for top-demand stylists"],
    risks: ["No-shows: send reminders a day before", "Hygiene/licensing compliance", "Depending on one star stylist"]
  },
  agriculture: {
    name: "Farming & agribusiness", icon: "🌾",
    ideas: ["Add value: dry, pack, juice or process produce", "Sell direct to restaurants, schools and hotels", "Farm-gate box subscriptions for city customers", "Join or form a cooperative for bulk inputs and transport"],
    marketing: ["Tell your farm story with photos of harvest and people", "Get on local market and WhatsApp buyer groups", "Simple brand and label for packaged products", "Attend agricultural fairs to meet bulk buyers"],
    money: ["Keep a record per crop/animal of cost vs. sale price", "Plant/sell for off-season higher prices where possible", "Look for agricultural grants, microloans and input subsidies", "Use contracts with buyers to secure price before harvest"],
    risks: ["Weather & pests: diversify crops and consider crop insurance", "Post-harvest loss: proper storage and drying", "Middlemen squeezing prices: build direct buyers"]
  },
  fashion: {
    name: "Fashion, tailoring & textiles", icon: "🧵",
    ideas: ["Made-to-measure with an online order form", "Small 'drops' of limited collections", "Uniform contracts for schools, churches, companies", "Repair & alteration service for steady income"],
    marketing: ["Model your clothes on real local customers", "Reels showing the making process", "Pop-up stands at markets and events", "Influencer gifting to micro-creators (1k–10k followers)"],
    money: ["Price = materials + labour hours × rate + overhead + profit (30%+)", "Take 50% deposit on custom orders", "Buy fabric in bulk for best sellers only", "Track which styles sell fastest"],
    risks: ["Late delivery: give realistic dates", "Fabric waste: plan cutting layouts", "Copycats: build a brand and community, not just designs"]
  },
  transport: {
    name: "Transport, delivery & logistics", icon: "🚚",
    ideas: ["Contracts with shops and restaurants for daily deliveries", "Scheduled routes (same area, same day) to cut costs", "Moving services for students and families", "Parcel pickup point partnership with a shop"],
    marketing: ["Branded vehicle: it's a moving billboard", "Fast WhatsApp quotes with fixed zone prices", "Reliability guarantee builds trust", "Google Business profile with reviews"],
    money: ["Track cost per km (fuel, maintenance, driver)", "Preventive maintenance is cheaper than breakdowns", "Price by zones and weight, add a fuel surcharge when fuel rises", "Get invoices paid within 7–14 days"],
    risks: ["Accidents & insurance", "Fuel price swings", "Late-paying clients: use deposits"]
  },
  digital: {
    name: "Tech, digital & creative services", icon: "💻",
    ideas: ["Productize: fixed-price packages instead of hourly", "Monthly retainers for social media/website care", "Templates and digital products for passive income", "Teach a short workshop for other small businesses"],
    marketing: ["Portfolio with 3 strong case studies with results", "LinkedIn + niche-focused content (e.g. 'websites for salons')", "Partnerships with accountants, printers, agencies", "Free 15-min audit as lead magnet"],
    money: ["50% upfront, 50% on delivery", "Raise prices for every new client until 1 in 4 says no", "Recurring revenue target: 50% of income", "Track hours per project to find unprofitable work"],
    risks: ["Scope creep: written scope and change fees", "Single big client dependency", "Burnout: block focus time"]
  },
  trades: {
    name: "Construction & home trades", icon: "🔨",
    ideas: ["Maintenance plans for homes and offices", "Specialize (e.g. solar installs, waterproofing)", "Partner with hardware stores for referrals", "Emergency call-out service at premium price"],
    marketing: ["Before/after job photos", "Vehicle and uniform branding", "Ask every client for a review and 2 referrals", "Listing on local directories and Google Maps"],
    money: ["Written quotes with materials and labour separated", "Deposit for materials before starting", "Track profit per job", "Buy materials on trade accounts with discounts"],
    risks: ["Safety and insurance", "Underquoting: add 10–15% contingency", "Late payment: staged payments by milestone"]
  },
  education: {
    name: "Education, tutoring & training", icon: "📚",
    ideas: ["Small group classes (better income per hour)", "Exam prep bootcamps before exam season", "Online courses or recorded lessons", "Holiday clubs and skills camps"],
    marketing: ["Share student results (with permission)", "Free trial lesson", "Parent WhatsApp groups and school notice boards", "Short tips videos on social media"],
    money: ["Packages paid monthly or per term in advance", "Sibling and referral discounts", "Track retention: who renews each term", "Use free tools (Google Classroom, Meet)"],
    risks: ["Seasonal demand: plan holiday offers", "Child safety policies", "Cancellations: clear policy"]
  },
  health: {
    name: "Health, pharmacy & wellness", icon: "💊",
    ideas: ["Wellness checks (blood pressure, sugar) to bring footfall", "Home delivery of repeat prescriptions", "Fitness/wellness memberships", "Corporate wellness days"],
    marketing: ["Health tips content builds trust", "Partner with local clinics and gyms", "Reminders for refills by SMS", "Community health talks"],
    money: ["Monitor expiry dates and rotate stock", "Focus on high-margin wellness products", "Membership for steady cash flow", "Negotiate with wholesalers as a buying group"],
    risks: ["Licensing and regulation must be up to date", "Expired stock losses", "Patient data privacy"]
  },
  hospitality: {
    name: "Tourism, hospitality & events", icon: "🏨",
    ideas: ["Local experience tours (food, culture, nature)", "Packages with partner restaurants and guides", "Off-season offers for locals", "Event space rental on weekdays"],
    marketing: ["Booking.com/Airbnb/Google listing with great photos", "Respond to every review", "Partner with travel bloggers", "Direct-booking discount to avoid commissions"],
    money: ["Dynamic pricing: higher at peak, deals in low season", "Track occupancy and revenue per room/seat", "Deposits for bookings", "Upsell extras: breakfast, transport, tours"],
    risks: ["Seasonality", "Bad reviews: fix issues fast", "Cancellations: clear policy"]
  },
  crafts: {
    name: "Crafts, art & handmade", icon: "🎨",
    ideas: ["Sell on Etsy/online marketplaces and your own shop", "Custom/personalised gifts", "Workshops teaching your craft", "Wholesale to gift shops and hotels"],
    marketing: ["Story behind each piece and the maker", "Process videos", "Craft fairs and markets", "Gift-season campaigns (holidays, Mother's Day)"],
    money: ["Price for your time: materials × 2 + hourly labour", "Make batches to save time", "Keep a best-seller line plus limited editions", "Track material costs per piece"],
    risks: ["Underpricing your time", "Shipping damage: good packaging", "Inconsistent supply of materials"]
  },
  other: {
    name: "Other / not listed", icon: "✨",
    ideas: ["List your 3 best customers and ask what else they'd pay for", "Turn your most-asked question into a paid service", "Recurring offer (subscription, maintenance, membership)", "Partner with a business that serves the same customers"],
    marketing: ["Google Business profile + reviews", "Consistent posts: 3 per week", "Referral reward", "Talk to 5 customers every week"],
    money: ["Separate business and personal money", "Know your monthly break-even", "Keep 3 months of costs as an emergency fund", "Review prices every 6 months"],
    risks: ["Cash flow gaps", "Relying on one customer or supplier", "No written records"]
  }
};
