FROM python:alpine

RUN  apk add --no-cache gcc musl-dev libffi-dev libev-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN  pip install --no-cache-dir -r requirements.txt
RUN  pip install gunicorn bjoern cheroot #wsgi servers

COPY . /usr/src/app

EXPOSE 5000
CMD [ "python", "-m", "flask", "run" ]

#  vim: set ts=8 sw=4 tw=0 ft=dockerfile :
