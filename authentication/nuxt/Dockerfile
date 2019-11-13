FROM node:10.15-alpine as builder
WORKDIR /app
ENV NODE_ENV=production
ADD ./package.json ./
RUN yarn --frozen-lockfile --non-interactive
ADD ./ ./
RUN yarn build


## Multi-Stage Build
FROM node:10.15-alpine
WORKDIR /app
ENV HOST=0.0.0.0

ADD package.json ./
ADD nuxt.config.js ./

COPY --from=builder ./app/node_modules ./node_modules/
COPY --from=builder ./app/.nuxt ./.nuxt/
COPY --from=builder ./app/static ./static/

CMD ["yarn", "start"]
