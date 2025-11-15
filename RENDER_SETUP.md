# Render Deployment Guide for Hotel Booking System

## Prerequisites
- GitHub, GitLab, or Bitbucket account with your code
- Render.com account (free tier available)
- Git installed locally

## Step 1: Prepare Your Repository

Make sure all files are committed:
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main-myproject
```

## Step 2: Create PostgreSQL Database on Render

1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name:** `hotel-booking-db`
   - **Database:** `hotel_booking_project`
   - **User:** `hotel_booking_project`
   - **Plan:** Free (auto-pauses after 15 mins)
4. Copy the **Internal Database URL** (you'll need this later)

## Step 3: Create Web Service on Render

1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select `hotel_booking_project` repository

## Step 4: Configure Web Service Settings

### Basic Settings:
- **Name:** `hotel-booking-system`
- **Environment:** Python 3
- **Region:** Oregon (or your preferred region)
- **Plan:** Free (for testing) or Starter (for production)

### Build Command:
```bash
pip install --upgrade pip && pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Start Command:
```bash
gunicorn hotel_booking_project.wsgi:application --bind 0.0.0.0:$PORT --workers 3
```

## Step 5: Add Environment Variables

In Render dashboard, go to **Environment** and add:

| Key | Value |
|-----|-------|
| `DEBUG` | `False` |
| `SECRET_KEY` | *Generate a strong key (see below)* |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `DATABASE_URL` | *Paste the PostgreSQL URL from Step 2* |

### Generate SECRET_KEY:
Run this command locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output and paste it as `SECRET_KEY` in Render.

## Step 6: Deploy

1. Click **"Create Web Service"**
2. Render will automatically detect `render.yaml` and deploy
3. Monitor the build progress in the dashboard
4. Once deployed, visit your app at `https://your-app-name.onrender.com`

## Step 7: Run Initial Setup (First Time Only)

After deployment completes:
1. Go to your service in Render dashboard
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_rooms
```

## Important Notes

### Security
⚠️ **NEVER** commit `.env` files or secrets to Git
✅ Always use environment variables for sensitive data
✅ Set `DEBUG = False` in production

### Port Configuration
- Render automatically assigns `$PORT` (usually 10000)
- Your app listens on `0.0.0.0:$PORT`
- No need to hardcode port numbers

### Static Files
- Automatically collected during build
- Served by WhiteNoise middleware
- No additional configuration needed

### Database
- Free PostgreSQL tier included
- Auto-pauses after 15 mins of inactivity
- Upgrade to Starter plan for production use

## Troubleshooting

### 500 Error - Check Logs:
1. Go to Render dashboard
2. Click your service
3. View logs in real-time
4. Look for specific error messages

### Static Files Not Loading:
- Ensure `STATIC_URL = '/static/'` in settings
- Check that `collectstatic` ran successfully
- Verify `WhiteNoiseMiddleware` is in MIDDLEWARE

### Database Connection Error:
- Verify `DATABASE_URL` is correct
- Check database is running (not paused)
- Run migrations in Shell tab

### Import Errors:
- Verify all packages in `requirements.txt` are installed
- Check for typos in settings imports
- Run `pip install -r requirements.txt` locally to test

## Monitoring Your App

1. **Real-time Logs:** Dashboard → Logs tab
2. **Metrics:** Dashboard → Metrics tab (CPU, Memory, Disk)
3. **Error Alerts:** Setup in Dashboard settings
4. **Health Checks:** Render monitors app availability

## Cost Management (Free Tier)
- 750 free dyno hours/month
- Auto-sleep after 15 mins inactivity
- Limited storage (100 MB)
- Good for development/testing

For production, upgrade to Starter plan ($7/month per service)

## Redeployment

Every time you push to your GitHub branch, Render automatically redeploys:
```bash
git add .
git commit -m "Your changes"
git push origin main-myproject
```

---

**Your app will be live at:** `https://hotel-booking-system.onrender.com`

For more help, visit [Render Documentation](https://render.com/docs)
